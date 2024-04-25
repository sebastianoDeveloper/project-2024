from django.shortcuts import redirect, render
from encuesta.models import Informacion
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request,'principal.html')

def consultar(request):
  informacion = Informacion.objects.all()
  return render(request,'informacion.html',{
    'informacion': informacion
  })

def guardar(request):
  nombre = request.POST["nombre"]
  transporte = request.POST["transporte"]
  horario = request.POST["horario"]
  dni = request.POST["dni"]
  edad = request.POST["edad"]
  d = Informacion(nombre = nombre,transporte = transporte, horario = horario, dni = dni, edad = edad)
  d.save()
  messages.success(request, 'Información guardada')
  return redirect('consultar')

def eliminar(request,id):
  encontrado = Informacion.objects.filter(pk = id)
  encontrado.delete()
  messages.success(request, 'Información eliminada')
  return redirect('consultar')

def detalle(request, id):
    seleccionado = Informacion.objects.get(pk = id)
    return render(request, "informacionDetalle.html", {
      'seleccionado' : seleccionado
    })

def editar(request):
  nombre = request.POST["nombre"]
  transporte = request.POST["transporte"]
  horario = request.POST["horario"]
  dni = request.POST["dni"]
  edad = request.POST["edad"]
  id = request.POST["id"]
  Informacion.objects.filter(pk = id).update(id=id,nombre = nombre,transporte = transporte, horario = horario, dni = dni, edad = edad)
  messages.success(request, 'Información actualizada')
  return redirect('consultar')