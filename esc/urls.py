"""esc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
import estoque, vendas, estacionamento
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^estoque/', include('estoque.urls', namespace = 'estoque')),
    url(r'^vendas/', include('vendas.urls', namespace = 'vendas')),
    url(r'^estacionamento/', include('estacionamento.urls', namespace = 'estacionamento')),
    url(r'^financeiro/', include('financeiro.urls', namespace = 'financeiro')),
    url(r'^$', views.index, name='index'),
    
]
