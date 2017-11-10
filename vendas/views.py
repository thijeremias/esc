#-*-coding: utf8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .forms import vendaForm, fpForm, consultarVendaForm, m2mForm
from django.http import JsonResponse, HttpResponse
from estoque.models import Produto
from .models import Vendas, venda_produtos
import json
from django.core import serializers
from django.db.models import Q
from .utils import render_to_pdf, create_table

# Create your views here.

def vendas(request):
    context = {}
    if request.method == 'POST':
        venda = vendaForm(request.POST)
        if venda.is_valid():
            venda.save()
            create_table(request.POST.getlist('produto_id'),request.POST.getlist('quantidade'))
            return redirect('vendas:imprimir')
        else:
             context['form'] = venda
    else:
        context['form2'] = m2mForm()
        context['form'] = vendaForm()
    return render(request, 'vendas/vendas.html', context)

def cadastrar_fp(request):
    context = {}
    if request.method == 'POST':
        fp = fpForm(request.POST)
        if fp.is_valid():
            fp.save()
            context['form'] = fpForm()
        else:
            context['form'] = fp
    else:
        context['form'] = fpForm()
    return render(request,'vendas/cadastrar_fp.html', context)

def consultar_vendas(request):
    context = {}
    if request.method == 'POST':
        context['vendas'] = Vendas.objects.filter(
            Q(data_emissao__iexact = request.POST.get('data_emissao')) |
            Q(id__iexact = request.POST.get('data_emissao'))
        )
        context['controle'] = 1
        return render(request,'vendas/consultar_vendas.html',context)
    else:
        context['form'] = consultarVendaForm()
    return render(request, 'vendas/consultar_vendas.html', context)
    
def excluir_vendas(request, pk):
    venda = Vendas.objects.filter(id__iexact=pk)
    venda.delete()
    return render(request,'vendas/consultar_vendas.html',{'form': consultarVendaForm()})

def imprimir(request):
    template_path = 'vendas/imprimir.html'
    context = {}
    context['vendas'] = Vendas.objects.last() 
    context['m2m'] = venda_produtos.objects.filter(venda_id=context['vendas'].id)
    return render_to_pdf(template_path,context)

def ajax_vendas(request):
    id_produto = request.GET['id']
    produtos = Produto.objects.filter(id=id_produto)
    data = serializers.serialize('json',produtos,fields=('valor'))
    return JsonResponse(data,safe=False)