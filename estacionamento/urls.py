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
from . import views

urlpatterns = [
    url(r'^cadastrar_cliente/$', views.cadastrar_cliente, name = 'cadastrar_cliente'),
    url(r'^cadastrar_veiculo/$', views.cadastrar_veiculo, name = 'cadastrar_veiculo'),
    url(r'^consultar_veiculo/$', views.consultar_veiculo, name = 'consultar_veiculo'),
    url(r'^editar_veiculo/(?P<pk>[0-9]+)/$', views.editar_veiculo, name = 'editar_veiculo'),
    url(r'^mensalistas/$', views.mensalistas, name = 'mensalistas'),
    url(r'^entrada/$', views.entrada, name = 'entrada'),
    url(r'^saida/$', views.saida, name = 'saida'),
    url(r'^config/$', views.config, name='config'),
    
    
    
]