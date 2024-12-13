from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.template import Template, Context, loader
from .models import Productos,Vendedor,Comprador,Devolucion
def inicio(request):
    return render(request,"WebApp/index.html")


def productos(request): 
    query = request.GET.get("q")
    if query:
        productos = Productos.objects.filter(Q(producto__icontains=query) | Q(unidades__icontains=query) | Q(precio__icontains=query))
    else:
        productos = Productos.objects.all()

    if request.method == "POST":
        new_producto = Productos(producto=request.POST["producto"], unidades=request.POST["unidades"], precio=request.POST["precio"])
        print('se hizo post')
        new_producto.save()
        productos = Productos.objects.all()
    return render(request, "WebApp/productos.html", {"productos": productos})

def vendedores(request):
    query = request.GET.get("q")
    if query:
        vendedores = Vendedor.objects.filter((Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query) | Q(codigo__icontains=query)))
    else:
        vendedores = Vendedor.objects.all()
    if request.method == "POST":
        vendedores = Vendedor(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"],codigo=request.POST["codigo"])
        print('se hizo post')
        vendedores.save()
        vendedores = Vendedor.objects.all()
    return render(request,"WebApp/vendedores.html",{"vendedores": vendedores})

def compradores(request):
    query = request.GET.get("q")
    if query:
        compradores = Comprador.objects.filter((Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query)))
    else:
        compradores = Comprador.objects.all()
    if request.method == "POST":
        compradores = Comprador(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"])
        print('se hizo post')
        compradores.save()
        compradores = Comprador.objects.all()
    return render(request,"WebApp/compradores.html",{"compradores": compradores})

def devoluciones(request):
    query = request.GET.get("q")
    if query:
        devoluciones = Devolucion.objects.filter((Q(producto__icontains=query) | Q(fechaDeEntrega__icontains=query) | Q(devuelto=query.lower() in ["true", "1", "on"])))
    else:
        devoluciones = Devolucion.objects.all()
    if request.method == "POST":
        devuelto = request.POST.get("devuelto") == "on"
        devoluciones = Devolucion(producto=request.POST["producto"],fechaDeEntrega=request.POST["fechaDeEntrega"],devuelto=devuelto)
        print('se hizo post')
        devoluciones.save()
        devoluciones = Devolucion.objects.all()
    return render(request,"WebApp/devoluciones.html",{"devoluciones": devoluciones})


def formulario_producto(request):
    if request.method == "POST":
        new_producto = Productos(producto=request.POST["producto"], unidades=request.POST["unidades"], precio=request.POST["precio"])
        print('se hizo post')
        new_producto.save()
        #return render(request,"WebApp/forms/formulario_curso.html")
        return redirect("productos")
    else:
        return render(request,"WebApp/forms/formulario_producto.html")