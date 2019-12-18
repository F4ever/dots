from django.shortcuts import render


# Create your views here.
def return_game_page(request):
    return render(request, 'templates/index.html')
