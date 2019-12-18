from django.contrib.auth import login

from core.models import User


class AnonimaizerUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated():
            user = User.objects.create_user(
                username=f'Anonim-{User.objects.count()}'
            )

            login(request, user)

        response = self.get_response(request)

        return response
