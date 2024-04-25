## COMANDOS

bajas django
---->
python -m pip install Django

bajas tu proyecto
---->
django-admin startproject conexion2

Para crear aplicacion/funcionalidades pequeñas
(te ubicas dentro ps)
---->
py manage.py startapp formulario

Para ejecutar
---->
py manage.py runserver

DD.BB
Va a 52
---->
py manage.py makemigrations
Para ejecutar
---->
py manage.py migrate

Para crear super usuario
---->
py manage.py createsuperuser

Bajando 200 datos a sqlite3
Entro a la shell de python
---->
py manage.py shell

Le importo el modelo
---->
from encuesta.models import Informacion

## EDITAR Y ACTUALIZAR

1. path('informacion/detalle/<int:id>', views.detalle, name='detalle' ),
2. path('informacion/editar', views.editar, name='editar' ),

el 1ro es para mostrar los datos en formulario de la casilla seleccionada
el 2do es para actualizar en si
en la vista editar, nisiquiera tengo k guardar en una variable xk la actualizacion sera tal cual aqui

## PUSH DE DATOS

### 1ra manera

nombre,horario,dni,edad,tra
enc1 = Informacion(nombre='Juan Perez',horario="08:00",dni=12345678,edad=30,transporte='Corrdor')
enc1.save()

### 2da manera

enc2=Informacion.objects.create(nombre='Julito Roman',horario="13:00",dni=33345678,edad=20,transporte='Corredor')

### 3ra manera

Informacion.objects.create(nombre='Emilia Sánchez', horario="08:30", dni=12345678, edad=27, transporte='Tren'),Informacion.objects.create(nombre='Lucas González', horario="11:15", dni=23456789, edad=29, transporte='Corredor'),Informacion.objects.create(nombre='Martina Pérez', horario="13:45", dni=34567890, edad=31, transporte='Metropolitano'),Informacion.objects.create(nombre='Santiago López', horario="10:20", dni=45678901, edad=26, transporte='Tren'),
