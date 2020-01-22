from django.urls import re_path

from core.views import ProfileViewSet
from room.views import RoomViewSet, UserJoinViewSet, PlayedRoomViewSet, DoneRoomViewSet


urlpatterns = [
    re_path(r'^me/$', ProfileViewSet.as_view({'get': 'retrieve'})),

    re_path(r'^rooms/$', RoomViewSet.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'^rooms/(?P<pk>\d+)/$', RoomViewSet.as_view({'get': 'retrieve'})),

    re_path(r'^join/$', UserJoinViewSet.as_view({'post': 'create'})),

    re_path(r'^rooms/played/$', PlayedRoomViewSet.as_view({'get': 'list'})),
    re_path(r'^rooms/done/$', DoneRoomViewSet.as_view({'get': 'list'})),
]
