from django import forms
from .models import Caixa, ContasReceber

class caixaForm(forms.ModelForm):
    class Meta:
        model = Caixa
        fields = ('__all__')
        widgets = {
            'movimento': forms.Select(attrs = {'class': 'form-control'}),
            'descricao': forms.TextInput(attrs = {'class': 'form-control'}),
            'valor': forms.NumberInput(attrs = {'class': 'form-control'}),
            'data_pagamento': forms.TextInput(attrs = {'class': 'form-control',
                                                       'readonly': True
            })
        }

class contasReceberForm(forms.ModelForm):
    class Meta:
        model = ContasReceber
        fields = ('veiculo', 'mes', 'data_pagamento')
        widgets = {
            'veiculo': forms.Select(attrs = {'class': 'form-control'}),
            'mes': forms.Select(attrs = {'class': 'form-control'}),
            'data_pagamento': forms.TextInput(attrs = {'class': 'form-control',
                                                       'readonly': True
            }),
        }
        
class borderoForm(forms.ModelForm):
    class Meta:
        model = Caixa
        fields = ('data_pagamento',)
        widgets = {
            'data_pagamento': forms.TextInput(attrs = {'class': 'form-control',})
        }