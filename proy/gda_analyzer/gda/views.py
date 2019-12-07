from django.shortcuts import render, redirect

from gda.models import *


class IGDA:

    def __init__(self, energia, grasa, grasa_sat, hde_carbono, azucares_adicionados, azucares_totales, proteina,
                 fibra_nsp, fibra_aoac, sodio, sal):
        self.energia = energia
        self.grasa = grasa
        self.grasa_saturada = grasa_sat
        self.otras_grasas = grasa - grasa_sat
        self.hde_carbono = hde_carbono
        self.azucares_adicionados = azucares_adicionados
        self.azucar_total = azucares_totales
        self.proteina = proteina
        self.fibra_nsp = fibra_nsp
        self.fibra_aoac = fibra_aoac
        self.sodio = sodio
        self.sal = sal


# IGDA Adultos
gda_adultos_mujeres = IGDA(
    2000, 70, 20, 230, 50,
    90, 45, 18, 24, 2.4, 6
)

gda_adultos_hombres = IGDA(
    2500, 95, 30, 300, 65,
    120, 56, 18, 24, 2.4, 6
)

# IGDA Niñas 4-6 años
gda_ninas_46 = IGDA(
    1550, 60, 20, 195, 40,
    75, 20, 9, 12, 1.1, 3
)
# IGDA Niñas 7-10 años
gda_ninas_710 = IGDA(
    1750, 70, 20, 220, 50,
    85, 28, 12, 16, 1.8, 5
)

# IGDA Niñas 11-14 años
gda_ninas_1114 = IGDA(
    1850, 70, 25, 230, 50,
    90, 41, 15, 20, 2.4, 6
)

# IGDA Niñas 11-14 años
gda_ninas_1518 = IGDA(
    2100, 80, 25, 265, 60,
    105, 45, 18, 24, 2.4, 6
)

# IGDA Niños 4-6 años
gda_ninos_46 = IGDA(
    1700, 65, 20, 215, 45,
    85, 20, 9, 12, 1.1, 3
)
# IGDA Niños 7-10 años
gda_ninos_710 = IGDA(
    1950, 75, 25, 245, 55,
    100, 28, 12, 16, 1.8, 5
)

# IGDA Niños 11-14 años
gda_ninos_1114 = IGDA(
    2200, 85, 25, 275, 60,
    110, 42, 15, 20, 2.4, 6
)

# IGDA Niños 11-14 años
gda_ninos_1518 = IGDA(
    2750, 105, 35, 345, 75,
    140, 55, 18, 24, 2.4, 6
)


def grafica_datos(request, *args, **kwargs):
    consumos = Consumo.objects.all()
    context = {
        "consumos": consumos,
        "info_gda": gda_adultos_mujeres,
    }
    return render(request, 'gda/charts.html', context)


def agregar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    consumo = Consumo()
    consumo.producto = producto
    consumo.save()
    return redirect('/gda/grafica')


def lista_productos(request, *args, **kwargs):
    productos = Producto.objects.all()
    context = {
        "productos": productos
    }
    return render(request, 'gda/tables.html', context)


def eliminar_consumo(request, id):
    consumo = Consumo.objects.get(pk=id)
    consumo.delete()
    return redirect('/gda/grafica')
