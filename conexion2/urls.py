"""
URL configuration for conexion2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from encuesta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='inicio' ),
    path('informacion', views.consultar, name='consultar' ),
    path('informacion/guardar', views.guardar, name='guardar' ),
    path('informacion/eliminar/<int:id>', views.eliminar, name='eliminar' ),
    path('informacion/detalle/<int:id>', views.detalle, name='detalle' ),
    path('informacion/editar', views.editar, name='editar' ),
]
