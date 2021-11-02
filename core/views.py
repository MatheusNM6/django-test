from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><body><h1>teste minha aplicação. Matheus está testando isso</h1></body></html>")


def produtos(request):
    return HttpResponse("<html><body><h1>Produtos</h1><h1>produto1</h1><h2>Produto2</h2><h3>Produto3</h3></body></html>")