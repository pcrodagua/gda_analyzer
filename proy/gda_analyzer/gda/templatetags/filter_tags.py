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


@register.filter(name='sub')
def sub(consumos, info_gda):
    return int(consumos) - int(info_gda)
