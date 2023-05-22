from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('carrito/', carrito, name="carrito"),
    path('iniciomensual/', iniciomensual, name="iniciomensual"),
    path('iniciosusanual/', iniciosusanual, name="iniciosusanual"),
    path('login/', login, name="login"),
    path('nosotros/', nosotros, name="nosotros"),
    path('nosotroslogin/', nosotroslogin, name="nosotroslogin"),
    path('perfil/', perfil, name="perfil"),
    path('perfilmensual/', perfilmensual, name="perfilmensual"),
    path('perfilsuscritoanual/', perfilsuscritoanual, name="perfilsuscritoanual"),
    path('productologin/', productologin, name="productologin"),
    path('productos/', productos, name="productos"),
    path('registrarse/', registrarse, name="registrarse"),
    path('seguimiento/', seguimiento, name="seguimiento"),
    path('vistaadmin/', vistaadmin, name="vistaadmin"),
    path('vistalogin/', vistalogin, name="vistalogin"),

    #CRUD
    path('add/', add, name="add"),
    
]