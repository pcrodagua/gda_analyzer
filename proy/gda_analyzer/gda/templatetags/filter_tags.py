from gda.models import *
from gda.views import gda_adultos_mujeres
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
def get_percent(consumos, propiedad):
    valor = float(get_property(consumos, propiedad))
    info = gda_adultos_mujeres
    maximo = getattr(info, propiedad)
    porcentaje = (100 / maximo) * valor
    return "{0:.2f} %".format(porcentaje)

@register.filter(name='get_difference')
def get_difference(consumos, propiedad):
    # {{consumos|get_difference:'grasas_totales'}}
    valor = float(get_property(consumos, propiedad))
    info = gda_adultos_mujeres
    maximo = getattr(info, propiedad)
    return str(maximo - valor)