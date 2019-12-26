from django.conf.urls import url

from core.views import return_game_page


urlpatterns = [
    url(r'^$', return_game_page),
]
