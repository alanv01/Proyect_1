
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def add(request):
    return render(request, ('core/add.html'))

def index(request):
    
    productos = Producto.objects.all()
    data = {
        'productosAll': productos
    }

    return render(request, 'core/index.html', data)

def carrito(request):
    return render(request, ('core/carrito.html'))

def iniciomensual(request):
    return render(request, ('core/iniciomensual.html'))

def iniciosusanual(request):
    return render(request, ('core/iniciosusanual.html'))

def login(request):
    return render(request, ('core/login.html'))

def nosotros(request):
    return render(request, ('core/nosotros.html'))

def nosotroslogin(request):
    return render(request, ('core/nosotroslogin.html'))

def perfil(request):
    return render(request, ('core/perfil.html'))

def perfilmensual(request):
    return render(request, ('core/perfilmensual.html'))

def perfilsuscritoanual(request):
    return render(request, ('core/perfilsuscritoanual.html'))

def productologin(request):
    return render(request, ('core/productologin.html'))

def productos(request):
    return render(request, ('core/productos.html'))

def registrarse(request):
    return render(request, ('core/registrarse.html'))

def seguimiento(request):
    return render(request, ('core/seguimiento.html'))

def vistaadmin(request):
    return render(request, ('core/vistaadmin.html'))

def vistalogin(request):
    return render(request, ('core/vistalogin.html'))



#CRUD
def add(request):
    data = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # CAPTURAMOS LA INFO DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() # INSERT INTO producto VALUES()
            data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/add.html', data)


def update(request, id):
    producto = Producto.objects.get(id=id) # SELECT CON WHERE (BUSCAR)
    data = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() # INSERT INTO producto VALUES()
            #data['msj'] = "Producto modificado correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario # MOSTRAR EN LA VISTA LOS CAMBIOS

    return render(request, 'core/update-product.html', data)

def delete(request, id):
    producto = Producto.objects.get(id=id) # SELECT CON WHERE (BUSCAR)
    producto.delete()

    return redirect(to="index")