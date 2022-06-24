from multiprocessing import context
from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    
    context = {
        'nome': 'Michel Souza Santana - GUi',
        'curso': 'Programação Web Com Django Framework',
        'fone': 'WhatsApp: (47) 9 9665-8601',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)
