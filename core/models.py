from secrets import choice
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Categoria(models.Model):
    #id -- > numero autoincrementable , Django lo hace por nosotros
    nombre = models.CharField(max_length=80)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idproducto = models.IntegerField()
    nombre = models.CharField(max_length=200)
    valor = models.IntegerField(default=5000)
    anio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    descripcion = models.TextField(null=True, blank=True)  
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre