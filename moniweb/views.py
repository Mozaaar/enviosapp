# moniweb/views.py
# moniweb/views.py
from django.shortcuts import render
from .models import Departamento, Ciudad, Transportista, Producto  # Asegúrate de importar los modelos necesarios

def menu_vista(request):
    departamentos = Departamento.objects.all()
    ciudades = Ciudad.objects.all()
    transportistas = Transportista.objects.all()
    productos = Producto.objects.all()

    opciones = {
        'Departamentos': departamentos,
        'Ciudades': ciudades,
        'Transportistas': transportistas,
        'Productos': productos,
    }
    return render(request, 'menu.html', {'opciones': opciones})
def departamento_vista(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    return render(request, 'departamento.html', {'departamento': departamento})

def ciudad_vista(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    return render(request, 'ciudad.html', {'ciudad': ciudad})

def transportista_vista(request, id):
    transportista = get_object_or_404(Transportista, id=id)
    return render(request, 'transportista.html', {'transportista': transportista})

def producto_vista(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto.html', {'producto': producto})