#-*-coding: utf8 -*-
from django.db import models
from datetime import date

# Create your models here.

class Marca(models.Model):
    descricao = models.CharField('Marca', max_length = 30)
    class Meta:
        ordering = ['descricao']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    
    def __str__(self):
        return self.descricao
        
class Produto(models.Model):
    descricao = models.CharField('Descrição', max_length = 30)
    quantidade = models.IntegerField('Quantidade')
    valor = models.DecimalField('Valor', max_digits = 6, decimal_places = 2)
    valor_compra = models.DecimalField('Valor de Compra', max_digits = 6, decimal_places = 2)
    produto_marca = models.ForeignKey(Marca, on_delete = models.CASCADE,verbose_name = 'Marca')
    criacao = models.DateTimeField('Criação', auto_now_add = True)
    ativo = models.BooleanField('Ativo', default = True)
    objects = models.Manager()
    class Meta:
        ordering = ['descricao']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def __str__(self):
        return self.descricao