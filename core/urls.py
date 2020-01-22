from django.urls import re_path

from core.views import return_game_page


urlpatterns = [
    re_path(r'^$', return_game_page),
]
