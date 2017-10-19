#-*-coding: utf8 -*-
from django import forms
from .models import Marca, Produto

class marcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs = {'class': 'form-control',
                                                  'placeholder': 'Ex: Petrobrás'
        }),
        }

class produtoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('descricao', 'quantidade', 'valor_compra', 'valor', 'produto_marca','ativo')
        widgets = { 
                    'descricao': forms.TextInput(attrs = {'class': 'form-control',
                                                          'placeholder': 'Ex: Óleo para motor VW'
                    }),
                    'quantidade': forms.TextInput(attrs = {'class': 'form-control',
                                                           'placeholder': 'Ex: 12'
                    }),
                    'valor_compra': forms.NumberInput(attrs = {'class': 'form-control',
                                                             'placeholder': 'Ex: 24,90'
                    }),
                    'valor': forms.NumberInput(attrs = {'class': 'form-control', 
                                                      'placeholder': 'Ex: 24,90'
                    }),
                    'produto_marca': forms.Select(attrs = {'class': 'form-control'}),
                    'ativo': forms.CheckboxInput()
            }
    

class produtoConsultaForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('descricao','ativo')
        widgets = { 
                    'descricao': forms.TextInput(attrs = {'class': 'form-control'}),
                    'ativo': forms.CheckboxInput()
            }
    