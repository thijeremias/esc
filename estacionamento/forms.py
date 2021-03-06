#-*-coding: utf8 -*-
from django import forms
from .models import Cliente, Veiculo, Config, Entrada, Saida

class configForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = ('valor_hora','valor_hora_moto')
        widgets = {
            'valor_hora': forms.NumberInput(attrs = {'class': 'form-control',
                                                  'placeholder': 'Ex: 0,00'
        }),
            'valor_hora_moto': forms.NumberInput(attrs = {'class': 'form-control',
                                                  'placeholder': 'Ex: 0,00'
        }),
        }

class veiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('__all__')
        widgets = { 
                'proprietario': forms.Select(attrs = {'class': 'form-control',}),
                'marca': forms.Select(attrs = {'class': 'form-control',}),
                'modelo': forms.TextInput(attrs = {'class': 'form-control',
                                                   'placeholder': 'Ex: Uno Fire'
                }),
                'placa': forms.TextInput(attrs = {'class': 'form-control', 
                                                  'placeholder': 'Ex: OQR1364'
                    }),
                'cor': forms.TextInput(attrs = {'class': 'form-control',
                                                'placeholder': 'Ex: branco'
                }),
                'mensalista': forms.CheckboxInput(),
                'valor': forms.NumberInput(attrs = {'class': 'form-control',
                                                    'placeholder': 'Ex: 0,90'
                })
                
            }

class veiculoForm2(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('__all__')
        widgets = { 
                'proprietario': forms.Select(attrs = {'class': 'form-control',}),
                'marca': forms.Select(attrs = {'class': 'form-control',}),
                'modelo': forms.TextInput(attrs = {'class': 'form-control',
                                                   'readonly': True
                }),
                'placa': forms.TextInput(attrs = {'class': 'form-control', 
                                                  'readonly': True
                    }),
                'cor': forms.TextInput(attrs = {'class': 'form-control',
                                                'readonly': True
                }),
                'mensalista': forms.CheckboxInput(attrs = {'readonly': True}),
                'valor': forms.NumberInput(attrs = {'class': 'form-control',
                                                    'readonly': True
                })
                
            }
            
class consultaVeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('placa',)
        widgets = {
            'placa': forms.TextInput(attrs = {'class': 'form-control', 
                                                  'placeholder': 'Ex: OQR1364'
                    }),
        }

class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')
        widgets = { 
                    'nome': forms.TextInput(attrs = {'class': 'form-control'}),
                    'cpf': forms.TextInput(attrs = {'class': 'form-control',
                                                    'placeholder': 'Ex: 01234567890'
                    }),
                    'tel1': forms.TextInput(attrs = {'class': 'form-control',
                                                     'placeholder': 'Ex: 38991416235'
                    }),
                    'tel2': forms.TextInput(attrs = {'class': 'form-control'})
            }

class entradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('placa', 'datetime', 'tipo')
        widgets = {
                  'placa': forms.TextInput(attrs = {'class': 'form-control',
                                                    'placeholder': 'Ex: OQR1364'
                  }),
                  'datetime': forms.TextInput(attrs = {'class': 'form-control',
                                                      'readonly': True,
                  }),
                  'tipo': forms.RadioSelect()
        }

class saidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ('placa', 'datetime')
        widgets = {
                  'placa': forms.Select(attrs = {'class': 'form-control'}),
                  'datetime': forms.TextInput(attrs = {'class': 'form-control',
                                                      'readonly': True 
                  })
        }