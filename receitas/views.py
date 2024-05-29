from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'receitas/paginas/home.html', context={'name': 'Marcos Cruz',})

