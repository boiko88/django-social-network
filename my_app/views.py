from django.shortcuts import render


def mainPage(request):
    return render(request, 'main.html')


def signup(request):
    return render(request, 'signup.html')