from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.serializers import ProfileSerializer


def return_game_page(request):
    return render(request, 'templates/index.html')


class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user
