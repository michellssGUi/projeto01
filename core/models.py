from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Estoque')
    
    def __str__(self):
        return self.nome
