from django.shortcuts import render
from django.http import HttpResponse
from .models import perfume, maquillaje, skinCare, capilar, accesorio

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

#registrar los accesos para poder acceder
def Perfumes(request):
    perfumes = perfume.objects.all()
    return render(request, 'perfumes/index.html', {'perfumes': perfumes})

def crear_perfume(request):
    return render(request, 'perfumes/crear.html')
def maquillaje(request):
    return render(request, 'perfumes/maquillaje.html')
def crear_maq(request):
    return render(request, 'perfumes/crear_maq.html')
def Capilares(request):
    return render(request, 'capilares.html')
def crear_capilares(request):
    return render(request, 'perfumes/crear_capilares.html')
def skin_care(request):
    return render(request, 'perfumes/skin_care.html')
def crear_skinCare(request):
    return render(request, 'perfumes/crear_skinCare.html')
def accesorios(request):
    return render(request, 'perfumes/accesorios.html')
def crear_accesorios(request):
    return render(request, 'perfumes/crear_accesorios.html')
def editar(request):
    return render(request, 'perfumes/editar.html')

