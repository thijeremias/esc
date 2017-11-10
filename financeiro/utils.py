from .models import Caixa, ContasReceber
from django.db.models import Sum

def entrada(data_inicial,data_final):
    resultado={}
    receber = ContasReceber.objects.filter(data_pagamento__gte=data_inicial,
    data_pagamento__lte=data_final)
    caixa_entrada = Caixa.objects.filter(data_pagamento__gte=data_inicial,
    data_pagamento__lte=data_final,movimento = 0)
    v1 = receber.aggregate(Sum('valor'))
    v2 = caixa_entrada.aggregate(Sum('valor'))
    if v1['valor__sum'] is None:
        v1['valor__sum'] = 0
    if v2['valor__sum'] is None:
        v2['valor__sum'] = 0
    resultado['total_entrada'] = v1['valor__sum'] + v2['valor__sum']
    resultado['receber'] = receber
    resultado['caixa_entrada'] = caixa_entrada
    return resultado
    
def saida(data_inicial,data_final):
    resultado = {}
    caixa_saida = Caixa.objects.filter(data_pagamento__gte=data_inicial,
    data_pagamento__lte=data_final,movimento = 1)
    total_saida = caixa_saida.aggregate(Sum('valor'))
    if total_saida['valor__sum'] is None:
        total_saida['valor__sum'] = 0
    resultado['total_saida'] = total_saida['valor__sum']
    resultado['caixa_saida'] = caixa_saida
    return resultado