from multiprocessing import context
from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

def index(request):
    produtos = Produto.objects.all()
    
    context = {
        'nome': 'Michel Souza Santana - GUi',
        'curso': 'Programação Web Com Django Framework',
        'fone': 'WhatsApp: (47) 9 9665-8601',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)