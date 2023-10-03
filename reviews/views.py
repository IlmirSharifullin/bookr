from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "base.html")


def search(request: HttpRequest):
    search = request.GET.get('search')
    return render(request, 'search.html', {'search': search})
