#-*-coding: utf8 -*-
from django.db import models
from estoque.models import Marca
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField("Nome", max_length = 35)
    cpf = models.CharField("CPF", max_length = 11, unique = True)
    tel1 = models.CharField("Telefone", max_length = 11)
    tel2 = models.CharField("Telefone 2", max_length = 11, blank = True, null = True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome',]
    
    def __str__(self):
        return self.nome

class Config(models.Model):
    valor_hora = models.DecimalField("Valor Hora", max_digits = 6, decimal_places = 2)
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Configuração"
        verbose_name_plural = "Configurações"
        
    def __str__(self):
        return "Valor da hora"
        
class Veiculo(models.Model):
    proprietario = models.ForeignKey(Cliente,on_delete = models.CASCADE, verbose_name = 'Proprietário')
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE, verbose_name = 'Marca')
    modelo = models.CharField('Modelo', max_length = 20)
    placa = models.CharField('Placa do veículo', max_length = 7)
    cor = models.CharField('Cor do veículo', max_length = 10)
    mensalista = models.BooleanField('Mensalista', default = True)
    valor = models.DecimalField("Mensalidade", max_digits = 6, decimal_places = 2)
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['proprietario']
    
    def __str__(self):
        return self.proprietario.nome

class Entrada(models.Model):
    placa = models.CharField("Placa", unique=True, max_length = 7)
    datetime = models.DateTimeField("Data/Hora", default = timezone.now)
    ativo = models.BooleanField("Ativo", default = True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['datetime']
    
    def __str__(self):
        return self.placa

class Saida(models.Model):
    placa = models.ForeignKey(Entrada, on_delete = models.CASCADE, limit_choices_to = {'ativo': True}, verbose_name = 'Placa')
    datetime = models.DateTimeField("Data/Hora", default = timezone.now)
    objects = models.Manager()

    class Meta:
        verbose_name = "Saída"
        verbose_name_plural = "Saidas"
        #ordering = ['datetime']
    
    def __str__(self):
        return self.placa        