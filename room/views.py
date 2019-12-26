from django.db.models import Count
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from room.models import Room
from room.serializers import ActiveRoomSerializer, UserJoinSerializer, PlayedRoomSerializer, DoneRoomSerializer


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    lookup_field = 'pk'
    ordering = ['-created_at']


class RoomViewSet(BaseViewSet):
    queryset = Room.objects.filter(status=Room.Status.ACTIVE).annotate(user_played=Count('players', distinct=True))
    serializer_class = ActiveRoomSerializer

    def get_queryset(self):
        return self.queryset.exclude(players=self.request.user)


class PlayedRoomViewSet(BaseViewSet):
    queryset = Room.objects.exclude(status=Room.Status.DONE)
    serializer_class = PlayedRoomSerializer

    def get_queryset(self):
        return self.queryset.filter(players=self.request.user)


class DoneRoomViewSet(BaseViewSet):
    queryset = Room.objects.filter(status=Room.Status.DONE)
    serializer_class = DoneRoomSerializer

    def get_queryset(self):
        return self.queryset.filter(players=self.request.user)


class UserJoinViewSet(BaseViewSet):
    queryset = Room.objects.all().annotate(user_played=Count('players', distinct=True))
    serializer_class = UserJoinSerializer
