from django.db import models
from datetime import date
from estoque.models import Produto, Marca
# Create your models here.

class FormadePagamento(models.Model):
    descricao = models.CharField('Descrição', max_length = 20)
    
    class Meta:
        ordering = ['descricao']
        verbose_name = 'Forma de pagamento'
        verbose_name_plural = 'Formas de pagamento'
    
    def __str__(self):
        return self.descricao
        
        
class Vendas(models.Model):
    valor = models.DecimalField('Valor', max_digits = 6, decimal_places = 2)
    desconto = models.DecimalField('Desconto', max_digits = 6, decimal_places = 2, blank = True, null = True)
    acrescimo = models.DecimalField('Acréscimo', max_digits = 6, decimal_places = 2, blank = True, null = True)
    data_emissao = models.DateField('Data de emissão', default = date.today())
    venda_produto = models.ManyToManyField(Produto,through = 'venda_produtos', limit_choices_to = {'ativo': True}, verbose_name = 'Produtos')
    venda_fp = models.ForeignKey(FormadePagamento, on_delete = models.CASCADE, verbose_name = 'Forma de pagamento')
    objects = models.Manager()
    class Meta:
        ordering = ['id']
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
    
    def __str__(self):
        return str(self.id)
        
class venda_produtos(models.Model):
    venda_id = models.ForeignKey(Vendas, on_delete = models.CASCADE, verbose_name = 'Venda')
    produto_id = models.ForeignKey(Produto, on_delete = models.CASCADE, verbose_name = 'Produto', blank = True)
    quantidade = models.IntegerField("Quantidade", blank = True)
    objects = models.Manager()
    
    def __str__(self):
        return str(self.id)