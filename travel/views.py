from django.shortcuts import render


def home(request):
    name = 'Alexander'
    return render(request, 'home.html', {'name': name})