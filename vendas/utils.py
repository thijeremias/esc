from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os
from estoque.models import Produto
from .models import Vendas, venda_produtos
from django.shortcuts import get_object_or_404

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path
    
def render_to_pdf(template_path, context):
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render(context)
    pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('Erro ao gerar PDF')
    return response

def diminui_quantidade(produto,qtd):
    produto.quantidade = produto.quantidade - int(qtd)
    produto.save()

def create_table(lista_produtos,lista_qtd):
    count = 0
    venda = Vendas.objects.last()
    for produto in lista_produtos:
        try:
            p = get_object_or_404(Produto, pk = produto)
        except:
            break
        diminui_quantidade(p,lista_qtd[count])
        m1 = venda_produtos(venda_id=venda,produto_id=p,quantidade=lista_qtd[count])
        m1.save()
        count = count + 1