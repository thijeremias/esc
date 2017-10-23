from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Marca, Produto
from .forms import marcaForm, produtoForm, produtoConsultaForm
from django.db.models import Q
# Create your views here.

def cadastrar(request):
    context = {}
    if request.method == 'POST':
        produto = produtoForm(request.POST)
        if produto.is_valid():
            produto.save()
            context['form'] = produtoForm()
        else:
            context['form'] = produto
    else:
        context['form'] = produtoForm()
    return render(request,'estoque/cadastrar.html',context)
    
def cadastrar_marca(request):
    context = {}
    if request.method == 'POST':
        marca = marcaForm(request.POST)
        if marca.is_valid():
            marca.save()
            context['form'] = marcaForm()
        else:
            context['form'] = marca
    else:
        context['form'] = marcaForm()
    return render(request, 'estoque/cadastrar_marca.html', context)

def consultar(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('ativo'):
            ativo = 1
        else:
            ativo = 0
        context['produtos'] = Produto.objects.filter(
            Q(ativo__iexact = ativo),
            Q(descricao__icontains = request.POST.get('descricao')) |
            Q(id__iexact = request.POST.get('descricao'))
        )
        context['controle'] = 1
        return render(request,'estoque/consultar.html',context)
    else:
        context['form'] = produtoConsultaForm()
    return render(request, 'estoque/consultar.html', context)

def editar(request, pk):
    context = {}
    produto = Produto.objects.get(id = pk)
    if request.method == 'POST':
        produto = produtoForm(request.POST, instance = produto)
        if produto.is_valid():
            produto.save()
            return redirect('estoque:consultar')
    else:
        context['form'] = produtoForm(instance = produto)
    return render(request,'estoque/editar.html',context)