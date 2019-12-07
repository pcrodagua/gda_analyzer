from django.urls import path
from gda import views

app_name = "gda"
urlpatterns = [
    path('productos', views.lista_productos, name='candidato'),
]