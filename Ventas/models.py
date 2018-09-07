from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Cliente(models.Model): # clientes 
    nombres = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()
    fecha_crea = models.DateTimeField(default=timezone.now,blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    def NombreCompleto(self):
		cadena="{0}  {1}"
		return cadena.format(self.nombres,self.apellidos)

    def __str__(self):
		return self.NombreCompleto()


class Producto(models.Model): # producto
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_unitario = models.IntegerField(blank=True, null=True)
   # Alumno=models.ForeignKey(Alumno,null=False,blank=False,on_delete=models.CASCADE)

    def Nombre(self):
		cadena="{0}"
		return cadena.format(self.nombre)

    def __str__(self):
		return self.Nombre()


class Venta(models.Model): # Venta
    producto = models.ForeignKey(Producto,null=False,blank=False,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE)
    precio_unitario = models.IntegerField(blank=True, null=True)
    cantidad=models.IntegerField(blank=True, null=True)
    precio_total = models.IntegerField(blank=True, null=True)
    estado_pago=models.BooleanField(default=False)
    fecha= models.DateTimeField(default=timezone.now,blank=True, null=True)
   # Alumno=models.ForeignKey(Alumno,null=False,blank=False,on_delete=models.CASCADE)

    def Nombre(self):
		cadena="{0}"
		return cadena.format(self.producto)

    def __int__(self):
		return self.cantidad


class Cartera(models.Model): # Cartera
    saldo = models.IntegerField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE)


    def __int__(self):
		return self.saldo

class Abono(models.Model): # Abono
    valor = models.IntegerField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta,null=False,blank=False,on_delete=models.CASCADE)
    fecha = models.DateField(blank=True, null=True)

    def __int__(self):
		return self.valor