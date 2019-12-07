from django.shortcuts import render
from gda.models import *

# Create your views here.

def lista_productos(request, *args, **kwargs):
    productos = Producto.objects.all()
    context = {
        "productos": productos
    }
    return render(request, 'gda/tables.html', context)
