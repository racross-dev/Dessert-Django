from django.shortcuts import render
# from django.http import HttpResponse
from .models import Producto

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def colecciones(request):
    return render(request, 'colecciones.html')

def top(request):
    datos = { 
        'productos' : Producto.objects.all()
    }
    return render(request, 'top.html', datos)

