
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_vista, name='menu'),
    path('departamento/<int:id>/', views.departamento_vista, name='departamento'),  # Ruta para un departamento específico
    path('ciudad/<int:id>/', views.ciudad_vista, name='ciudad'),  # Ruta para una ciudad específica
    path('transportista/<int:id>/', views.transportista_vista, name='transportista'),  # Ruta para un transportista específico
    path('producto/<int:id>/', views.producto_vista, name='producto'),  # Ruta para un producto específico
]
