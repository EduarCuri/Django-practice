"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import *
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludar),
    path('despedida/', despedida),
    path('saludo_con_parametro/<nombre>/<carrera>', saludo_con_parametro),
    path('despedida_con_parametros/<nombre>/<apellido>/<distrito>', despedida_con_parametros),
    path('primer_template/', primer_template),
    path('segundo_template/<nombreCompleto>/<especialidad>', segundo_template),
    path('mi-familia/', monstrar_familiares),
    path('blog/', index),
    

]
