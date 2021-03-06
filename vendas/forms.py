from django import forms
from .models import Vendas, FormadePagamento, venda_produtos

class m2mForm(forms.ModelForm):
    class Meta:
        model = venda_produtos
        fields = ('produto_id', 'quantidade')
        widgets = {
            'produto_id': forms.Select(attrs = {'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs = {'class': 'form-control'})
        }

class vendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ('data_emissao','venda_fp','desconto','acrescimo','valor')
        widgets = {
            'data_emissao': forms.TextInput(attrs = {'class': 'form-control',
                                                     'readonly': True,
            }),
            'venda_fp': forms.Select(attrs = {'class': 'form-control'}),
            'desconto': forms.NumberInput(attrs = {'class': 'form-control',
                                                   'placeholder': 'Ex: 9,90'
            }),
            'acrescimo': forms.NumberInput(attrs = {'class': 'form-control',
                                                    'placeholder': 'Ex: 9,90'
            }),
            'valor': forms.NumberInput(attrs = {'class': 'form-control'}),
            
            
        }

class fpForm(forms.ModelForm):
    class Meta:
        model = FormadePagamento
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs = {'class': 'form-control',
                                                  'placeholder': 'Ex: À vista',
            }),
        }
        
class consultarVendaForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ('data_emissao',)
        widgets = {
            'data_emissao': forms.TextInput(attrs = {'class': 'form-control'}),
        }

