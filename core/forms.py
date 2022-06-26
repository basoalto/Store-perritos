from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):
    class Meta:
         model = Producto
         fields = ['nombre', 'valor','anio', 'categoria', 'descripcion']


class CustomUserForm(UserCreationForm):
   
   class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
