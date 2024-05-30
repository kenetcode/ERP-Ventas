from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    email = models.EmailField()
    nombrecomercial = models.CharField(max_length=255)
    tipocliente = models.CharField(max_length=255)

class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=255)
    costo = models.FloatField()
    

class Venta(models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField()
    metodopago = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Servicio)
    total = models.FloatField()

class Factura(models.Model):
    numerofactura = models.IntegerField()
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)