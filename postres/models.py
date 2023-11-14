from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=60)
    presentacion = models.CharField(max_length=200)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion + " - " + self.presentacion
    
class Automoviles(models.Model):
    modelo = models.CharField(max_length=20)
    placa = models.CharField(max_length=7)
    chofer = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField(editable = True)  

    def __str__(self):
        return self.placa + " - " + self.modelo

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField(default=0000000000)  

    def __str__(self):
        return self.nombre
    
class Sucursales(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(default=0000000000)  
    horario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
