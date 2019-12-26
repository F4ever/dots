from django.db.models import Count
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from room.models import Room
from room.serializers import ActiveRoomSerializer, UserJoinSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().annotate(user_played=Count('players', distinct=True))
    serializer_class = ActiveRoomSerializer

    permission_classes = [IsAuthenticated]

    lookup_field = 'pk'
    ordering = ['-created_at']

    def get_queryset(self):
        return self.queryset.filter(status=Room.Status.ACTIVE).exclude(players=self.request.user)


class UserJoinViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().annotate(user_played=Count('players', distinct=True))
    serializer_class = UserJoinSerializer

    permission_classes = [IsAuthenticated]

    ordering = ['-created_at']
