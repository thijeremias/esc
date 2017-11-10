from .models import Entrada, Config
from django.utils import timezone

def calcula_tempo(placa):
    result = {}
    entrada = Entrada.objects.get(pk = placa)
    valorHora = Config.objects.first()
    result['resultado'] = timezone.now() - entrada.datetime
    if entrada.tipo == 0:
        result['tempo'] = (result['resultado'].seconds/3600)*60
        result['tempo'] = int(result['tempo'])
        result['resultado'] = (result['resultado'].seconds/3600)*float(valorHora.valor_hora)
        result['resultado'] = round(result['resultado'],2)
    else:
        result['tempo'] = (result['resultado'].seconds/3600)*60
        result['tempo'] = int(result['tempo'])
        result['resultado'] = (result['resultado'].seconds/3600)*float(valorHora.valor_hora_moto)
        result['resultado'] = round(result['resultado'],2)
    entrada.delete()
    return result