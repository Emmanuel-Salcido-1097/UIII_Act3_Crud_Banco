from django.shortcuts import render, redirect
from .models import Seguridad_Privada

# Create your views here.

def inicio_vista(request):
    sp = Seguridad_Privada.objects.all()
    return render(request, 'gestionarSeguridadPrivada.html', {'SeguridadP': sp})

def registrarSeguridadPrivada(request):
    Id_Seguridad =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    contacto = request.POST['txtcontacto']
    horarios = request.POST['txthorarios']
    personal = request.POST['txtpersonal']
    vehiculos = request.POST['txtvehiculos']
    servicios = request.POST['txtservicios']
     
    guardarSP = Seguridad_Privada.objects.create(Id_Seguridad=Id_Seguridad, nombre=nombre, contacto=contacto,
                                                    horarios=horarios, personal=personal, vehiculos=vehiculos, servicios=servicios)
    return redirect('/')

def seleccionarSeguridadPrivada( request, Id_Seguridad):
    SeguridadPrivada = Seguridad_Privada.objects.get(Id_Seguridad=Id_Seguridad)
    return render(request, 'editarSeguridadPrivada.html', {'SeguridadP': SeguridadPrivada})

def editarSeguridadPrivada(request):
    Id_Seguridad =  request.POST['txtid']
    nombre =  request.POST['txtnombre']
    contacto = request.POST['txtcontacto']
    horarios = request.POST['txthorarios']
    personal = request.POST['txtpersonal']
    vehiculos = request.POST['txtvehiculos']
    servicios = request.POST['txtservicios']
    
    SeguridadPrivada = Seguridad_Privada.objects.get(Id_Seguridad=Id_Seguridad)
    SeguridadPrivada.nombre = nombre
    SeguridadPrivada.contacto = contacto
    SeguridadPrivada.horarios = horarios
    SeguridadPrivada.personal = personal
    SeguridadPrivada.vehiculos = vehiculos
    SeguridadPrivada.servicios = servicios
    SeguridadPrivada.save()
    return redirect('/')

def borrarSeguridadPrivada(request,Id_Seguridad):
    SeguridadPrivada=Seguridad_Privada.objects.get(Id_Seguridad=Id_Seguridad)
    SeguridadPrivada.delete()
    return redirect("/")