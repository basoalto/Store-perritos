from telnetlib import STATUS
from django.shortcuts import render
from core.forms import ProductoForm, CustomUserForm
from django.shortcuts import redirect
from core.models import Producto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializer import ProductoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

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

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated))
def lista_productos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated))
def detalle_producto(request, id):
    
    try:
        producto =Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.mothod == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.mothod == 'DELETE':
         producto.delete()
         return Response(status.HTTP_204_NO_CONTENT)

# class ProductoViewSet(viewsets.ModelViewSet):
#     queryset = Producto.objects.all()
#     serializer_class = ProductoSerializer  