from django.urls import re_path

from room.views import RoomViewSet, UserJoinViewSet


urlpatterns = [
    re_path(r'^rooms/$', RoomViewSet.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'^rooms/(?P<pk>\d+)/$', RoomViewSet.as_view({'get': 'retrieve'})),

    re_path(r'^joins/$', UserJoinViewSet.as_view({'post': 'create'})),

    # url(r'^rooms/played/$', RoomViewSet.as_view({'get': 'list'})),
]
