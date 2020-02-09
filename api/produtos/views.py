from django.shortcuts import render
from .models import Produto


def home(request):
    name = 'Django MOC'
    products = Produto.objects.all()
    return render(request, 'produtos.html', {'name': name, 'products': products})


def product(request, code):
    product = Produto.objects.get(id=code)
    return render(request, 'produtos.html', {'product': product})
