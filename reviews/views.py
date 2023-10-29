from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Book


def welcome_view(request: HttpRequest):
    message = f'<html><h1>Welcome to Bookr!</h1>' \
              f'<p>{Book.objects.count()} books and counting!</p></html>'
    return HttpResponse(message)

