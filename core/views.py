from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><body><h1>teste minha aplicação. Matheus está testando isso</h1></body></html>")
