from django.db import models

class Productos (models.Model):
    producto = models.CharField(max_length=30)  
    unidades = models.IntegerField()
    precio = models.IntegerField()
    def __str__(self):
        return f"Nombre del Producto: {self.producto} - N° de Unidades: {self.unidades} - Precio del Producto: {self.precio}"

class Comprador (models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models. EmailField() 
    def __str__(self):
        return f"Nombre del Comprador: {self.nombre} - Apellido del Comprador: {self.apellido} - Email del Comprador: {self.email}"
    
class Vendedor (models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models. CharField(max_length=100)
    codigo = models.CharField(max_length=50) 
    def __str__(self):
        return f"Nombre del Vendedor: {self.nombre} - Apellido del Vendedor: {self.apellido} - Email del Vendedor: {self.email} - Codigo del Vendedor: {self.codigo}"

class Devolucion(models.Model):
    producto = models.CharField(max_length=100) 
    fechaDeEntrega = models.DateField() 
    devuelto = models. BooleanField() 
    def __str__(self):
        return f"Nombre del Producto: {self.producto} - Fecha de Devolucion: {self.fechaDeEntrega} - Devolucion {self.devuelto}"
