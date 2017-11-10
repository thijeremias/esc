from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import configForm, veiculoForm, clienteForm, entradaForm, saidaForm, consultaVeiculoForm, veiculoForm2
from .models import Veiculo, Config, Entrada
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from .utils import calcula_tempo

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
        context['result'] = calcula_tempo(request.POST.get('placa'))
        return render(request, 'estacionamento/saida.html',context)
    else:
        context['form'] = saidaForm()
        return render(request, 'estacionamento/saida.html',context)
        
def consultar_veiculo(request):
    context = {}
    if request.method == "POST":
        veiculo = Veiculo.objects.filter(placa__iexact = request.POST.get('placa'))
        context['veiculos'] = veiculo
        context['controle'] = 1
    else:
        context['form'] = consultaVeiculoForm()
    return render(request,'estacionamento/consultar_veiculo.html',context)

def editar_veiculo(request, pk):
    context = {}
    veiculo = Veiculo.objects.get(id = pk)
    if request.method == 'POST':
        veiculo = veiculoForm(request.POST, instance = veiculo)
        if veiculo.is_valid():
            veiculo.save()
            return redirect('estacionamento:consultar_veiculo')
    else:
        context['form'] = veiculoForm(instance = veiculo)
    return render(request,'estacionamento/editar_veiculo.html',context)