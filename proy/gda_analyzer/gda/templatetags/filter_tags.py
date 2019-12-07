from gda.models import *
from django import template

register = template.Library()

@register.filter(name='get_property')
def get_property(consumos, propiedad):
    valor = 0
    for consumo in consumos:
        producto = Producto.objects.get(pk=consumo.producto_id)
        valor = valor + getattr(producto, propiedad)
    return str(valor)

@register.filter(name='get_percent')
def get_percent(consumos, infoGda, propiedad):
    valor = get_property(consumos, propiedad)
    maximo = gettatr(infoGda, propiedad)
    porcentaje = (100 / maximo) * valor
    return porcentaje