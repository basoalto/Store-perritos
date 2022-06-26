from pyexpat import model
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):

      class Meta:
        model = Producto
        fields = ['nombre', 'valor', 'anio', 'categoria', 'descripcion']