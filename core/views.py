from django.shortcuts import render


def return_game_page(request):
    return render(request, 'templates/index.html')
