from django.contrib import admin

from room.models import Room, Dot, UserJoin


admin.site.register(Room)
admin.site.register(Dot)
admin.site.register(UserJoin)
