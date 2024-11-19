from django.shortcuts import render, redirect
from .models import Sucursales

# Create your views here.

def inicio_vista(request):
    su = Sucursales.objects.all()
    return render(request, 'gestionarSucursales.html', {'Su': su})

def registrarSucursales(request):
    Id_Sucursal =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    ubicacion = request.POST['txtubicacion']
    tamaño = request.POST['txttamaño']
    encargado = request.POST['txtencargado']
    horarios = request.POST['txthorarios']
    capacidad = request.POST['txtcapacidad']
    
    guardarSu = Sucursales.objects.create(Id_Sucursal=Id_Sucursal, nombre=nombre, ubicacion=ubicacion,
                                                    tamaño=tamaño, encargado=encargado, horarios=horarios, capacidad=capacidad)
    return redirect('/')

def seleccionarSucursales( request, Id_Sucursal):
    Sucursales_ = Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    return render(request, 'editarSucursales.html', {'Su': Sucursales_})

def editarSucursales(request):
    Id_Sucursal =  request.POST['txtid']
    nombre =  request.POST['txtnombre'] 
    ubicacion = request.POST['txtubicacion']
    tamaño = request.POST['txttamaño']
    encargado = request.POST['txtencargado']
    horarios = request.POST['txthorarios']
    capacidad = request.POST['txtcapacidad']
    
    Sucursales_ = Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    Sucursales_.nombre = nombre
    Sucursales_.ubicacion = ubicacion
    Sucursales_.tamaño = tamaño
    Sucursales_.encargado = encargado
    Sucursales_.horarios = horarios
    Sucursales_.capacidad = capacidad
    Sucursales_.save()
    return redirect('/')

def borrarSucursales(request,Id_Sucursal):
    Sucursales_=Sucursales.objects.get(Id_Sucursal=Id_Sucursal)
    Sucursales_.delete()
    return redirect("/")