from django.urls import path
from WebApp.views import inicio,productos,compradores,vendedores,devoluciones,formulario_producto
urlpatterns = [
    path('',inicio,name="inicio"),
    path('productos/',productos,name="productos"),
    path('compradores/',compradores,name="compradores"), 
    path('vendedores/',vendedores,name="vendedores"),
    path('devoluciones/',devoluciones,name="devoluciones"),
    path('formulario_producto/',formulario_producto,name="formulario_producto"),
]