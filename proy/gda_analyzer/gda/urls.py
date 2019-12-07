from django.urls import path
from gda import views

app_name = "gda"
urlpatterns = [
    path('productos', views.lista_productos, name='lista_productos'),
    path('grafica', views.grafica_datos, name='grafica_datos'),
    path('agregar/<int:id>', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:id>', views.eliminar_consumo, name='eliminar_consumo'),
    path('infogda', views.info_gda, name='info_gda'),
]