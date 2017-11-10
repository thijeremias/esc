from django.db import models
from estacionamento.models import Veiculo
from datetime import date

# Create your models here.
class ContasReceber(models.Model):
    MES_CHOICES = (
        (1,"Janeiro"),
        (2,"Fevereiro"),
        (3,"Março"),
        (4,"Abril"),
        (5,"Maio"),
        (6,"Junho"),
        (7,"Julho"),
        (8,"Agosto"),
        (9,"Setembro"),
        (10,"Outubro"),
        (11,"Novembro"),
        (12,"Dezembro"),
    )
    veiculo = models.ForeignKey(
        Veiculo, on_delete = models.CASCADE, limit_choices_to = {'mensalista': True}, 
        verbose_name = "Veiculo"
    )
    mes = models.IntegerField("Mês", choices = MES_CHOICES)
    data_pagamento = models.DateField("Data de Pagamento", default = date.today())
    valor = models.DecimalField("Valor", max_digits = 6, decimal_places = 2)
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Contas a Receber"
        verbose_name_plural = "Contas a Receber"
        ordering = ['data_pagamento',]
    
    def __str__(self):
        return self.veiculo.modelo

class Caixa(models.Model):
    MOVIMENTO_CHOICES = (
        (0,"ENTRADA"),
        (1,"SAIDA"),
    )
    movimento = models.IntegerField("Movimento", choices = MOVIMENTO_CHOICES)
    descricao = models.CharField("Descrição", max_length = 100)
    valor = models.DecimalField("Valor", max_digits = 6, decimal_places = 2)
    data_pagamento = models.DateField("Data de Pagamento", default = date.today())
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Caixa"
        verbose_name_plural = "Lançamentos"
        ordering = ['data_pagamento',]
    
    def __str__(self):
        return self.descricao