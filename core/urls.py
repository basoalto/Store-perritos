from email.mime import base
from xml.etree.ElementInclude import include
from django.db import router
from django.urls import path

from core.viewslogin import login
from .views import detalle_producto, home, base, galeria, listado_productos, nuevo_producto, modificar_producto, eliminar_producto, registro_usuario
from django.urls.conf import include

from .views import lista_productos
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('productos', lista_productos)

urlpatterns = [
    path('', home, name="home"),
    path('base/',base,name="base"),
    path('galeria/',galeria,name="galeria"),
    path('listado_productos/',listado_productos,name="listado_productos"),
    path('nuevo_producto/',nuevo_producto,name="nuevo_producto"),
    path('modificar_producto/<id>/',modificar_producto,name="modificar_producto"),
    path('eliminar_producto/<id>/',eliminar_producto,name="eliminar_producto"),
    path('registro/', registro_usuario, name='registro_usuario'),
    # path('api/', include(router.urls)),
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login', login, name='login'),
]    
