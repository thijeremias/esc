from django.shortcuts import render, redirect
from .forms import caixaForm, contasReceberForm
from .models import ContasReceber, Caixa
from .utils import entrada, saida
# Create your views here.

def contas_receber(request):
    context = {}
    if request.method == "POST":
        receber = contasReceberForm(request.POST)
        if receber.is_valid():
            receber = receber.save(commit = False)
            receber.valor = receber.veiculo.valor
            receber.save()
            context['form'] = contasReceberForm()
        else:
            context['form'] = receber
    else:
        context['form'] = contasReceberForm()
    return render(request,'financeiro/contas_receber.html',context)

def lancamentos(request):
    context = {}
    if request.method == "POST":
        lancamento = caixaForm(request.POST)
        if lancamento.is_valid():
            lancamento = lancamento.save()
            context['form'] = caixaForm()
        else:
            context['form'] = lancamento
    else:
        context['form'] = caixaForm()
    return render(request,'financeiro/lancamentos.html',context)

def bordero(request):
    context = {}
    if request.method == 'POST':
        data_inicial = request.POST.get('data_inicial')
        data_final = request.POST.get('data_final')
        context['entrada'] = entrada(data_inicial,data_final)
        context['saida'] = saida(data_inicial,data_final)
        context['saldo'] = context['entrada']['total_entrada'] - context['saida']['total_saida']
        context['controle'] = 1
    return render(request,'financeiro/bordero.html',context)

def consultar(request):
    context = {}
    if request.method == 'POST':
        data_inicial = request.POST.get('data_inicial')
        data_final = request.POST.get('data_final')
        movimento = request.POST.get('movimento')
        if movimento == "":
            context['lancamentos'] = Caixa.objects.filter(data_pagamento__gte=data_inicial,
            data_pagamento__lte=data_final)
        else:
            context['lancamentos'] = Caixa.objects.filter(data_pagamento__gte=data_inicial,
            data_pagamento__lte=data_final,movimento=movimento)
        context['controle'] = 1
    return render(request,'financeiro/consultar.html',context)

def excluir(request, pk):
    lancamento = Caixa.objects.filter(id__iexact=pk)
    lancamento.delete()
    return render(request,'financeiro/consultar.html')
