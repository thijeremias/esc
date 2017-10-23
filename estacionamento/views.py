from django.shortcuts import render
from django.http import HttpResponse
from .forms import configForm, veiculoForm, clienteForm, entradaForm, saidaForm
from .models import Veiculo, Config, Entrada
from django.db.models import Sum
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def config(request):
    context = {}
    valor_hora = Config.objects.first()
    if request.method == 'POST':
        valor_hora = configForm(request.POST, instance = valor_hora)
        if valor_hora.is_valid():
            valor_hora.save()
            context['form'] = valor_hora
    else:
        context['form'] = configForm(instance = valor_hora)
    return render(request,'estacionamento/config.html',context)

def cadastrar_cliente(request):
    context = {}
    if request.method == 'POST':
        cliente = clienteForm(request.POST)
        if cliente.is_valid():
            cliente.save()
            context['form'] = clienteForm()
        else:
            context['form'] = cliente
    else:
        context['form'] = clienteForm()
    return render(request,'estacionamento/cadastrar_cliente.html',context)

def cadastrar_veiculo(request):
    context = {}
    if request.method == 'POST':
        veiculo = veiculoForm(request.POST)
        if veiculo.is_valid():
            veiculo.save()
            context['form'] = veiculoForm()
        else:
            context['form'] = veiculo
    else:
        context['form'] = veiculoForm()
    return render(request,'estacionamento/cadastrar_veiculo.html',context)
    
def mensalistas(request):
    context = {}
    context['mensalistas'] = Veiculo.objects.filter(mensalista = True)
    context['quantidade'] = Veiculo.objects.filter(mensalista = True).count()
    context['valor_total'] = Veiculo.objects.aggregate(Sum('valor'))
    return render(request,'estacionamento/mensalistas.html',context)

def entrada(request):
    context = {}
    if request.method == 'POST':
        entrada = entradaForm(request.POST)
        if entrada.is_valid():
            entrada.save()
            context['form'] = entradaForm
        else:
            context['form'] = entrada
    else:
        context['form'] = entradaForm
    return render(request,'estacionamento/entrada.html',context)

def saida(request):
    context = {}
    if request.method == 'POST':
        entrada = Entrada.objects.get(pk = request.POST.get('placa'))
        valorHora = Config.objects.first()
        result = timezone.now() - entrada.datetime
        result = (result.seconds/3600)*float(valorHora.valor_hora)
        context['result'] = round(result,2)
        entrada.ativo = False
        entrada.save()
        return render(request, 'estacionamento/saida.html',context)
    else:
        context['form'] = saidaForm()
        return render(request, 'estacionamento/saida.html',context)