from email.mime import base
from django.urls import path
from .views import home, base, galeria, listado_productos, nuevo_producto, modificar_producto, eliminar_producto, registro_usuario


urlpatterns = [
    path('', home, name="home"),
    path('base/',base,name="base"),
    path('galeria/',galeria,name="galeria"),
    path('listado_productos/',listado_productos,name="listado_productos"),
    path('nuevo_producto/',nuevo_producto,name="nuevo_producto"),
    path('modificar_producto/<id>/',modificar_producto,name="modificar_producto"),
    path('eliminar_producto/<id>/',eliminar_producto,name="eliminar_producto"),
    path('registro/', registro_usuario, name='registro_usuario'),
]    
