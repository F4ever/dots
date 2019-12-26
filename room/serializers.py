from rest_framework import serializers

from room.models import Room, UserJoin, Dot


class ActiveRoomSerializer(serializers.ModelSerializer):
    user_played = serializers.IntegerField(read_only=True)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['creator'] = self.context['request'].user
        return validated_data

    class Meta:
        model = Room
        fields = (
            'id',
            'creator',
            'user_count',
            'status',
            'figure',
            'user_played',
        )
        read_only_fields = ['creator']


class DotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dot
        fields = (
            'abscissa',
            'ordinate',
        )


class UserJoinSerializer(serializers.ModelSerializer):
    dot = DotSerializer()

    class Meta:
        model = UserJoin
        fields = (
            'user',
            'room',
            'dot',
        )
        read_only_fields = ['user']

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['user'] = self.context['request'].user
        return validated_data

    def create(self, validated_data):
        new_dot = Dot.objects.create(**validated_data.pop('dot'))
        user_join, created = UserJoin.objects.update_or_create(**validated_data, defaults={'dot': new_dot})
        return user_join
