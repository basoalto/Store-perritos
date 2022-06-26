from django.shortcuts import render
from core.forms import ProductoForm, CustomUserForm
from django.shortcuts import render, redirect
from core.models import Producto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
# Create your views here.

from rest_framework import viewsets
from .serializer import ProductoSerializer

def home(request):
    return render(request, 'core/home.html')

def base(request):
    return render(request,'core/base.html')

def galeria(request):
    return render(request,'core/galeria.html')   


def listado_productos(request):
    productos = Producto.objects.all()
    data ={
        'productos':productos
    }
    return render(request,'core/listado_productos.html', data)

@permission_required('core.add_producto')
def nuevo_producto(request):
    data = {
        'form':ProductoForm()
    }

    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardando correctamente"


    return render(request,'core/nuevo_producto.html', data)  

@permission_required('core.add_producto')
def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "modificado correctamente"
            data['form'] = formulario
    return render(request,'core/modificar_producto.html', data)
@permission_required('core.add_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="listado_producto")



def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }

    if request.method == "POST":
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save();

            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, "registration/registrar.html", data) 


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer  