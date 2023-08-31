from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre   = models.CharField(max_length=30)
    contacto = models.CharField(max_length=30)
    email    = models.EmailField(null=True)
    cuit     = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.nombre}'
    class Meta():
        verbose_name = 'PROVEEDOR'
        verbose_name_plural = 'PROVEEDORES'
        
class Cliente(models.Model):
    nombre   = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fnasc    = models.DateField(null=True)
    email    = models.EmailField(null=True)
    dni      = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    class Meta():
        verbose_name = 'CLIENTE'
        verbose_name_plural = 'CLIENTES'
        
class RubroProd(models.Model):
    nombre   = models.CharField(max_length=30, null=True)
    def __str__(self):
        return f'{self.nombre}'
    class Meta():
        verbose_name = 'RUBRO'
        verbose_name_plural = 'RUBROS'
        
class Producto(models.Model):
    nombre   = models.CharField(max_length=30)
    rubro    = models.ForeignKey(RubroProd, on_delete=models.DO_NOTHING)
    proveedor= models.ForeignKey(Proveedor, on_delete=models.DO_NOTHING)
    precio   = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    def __str__(self):
        return f'{self.nombre}'
    class Meta():
        verbose_name = 'PRODUCTO'
        verbose_name_plural = 'PRODUCTOS'

class OrdenCompra(models.Model):
    comprador = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    producto  = models.ManyToManyField(Producto)
    cantidad  = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    class Meta():
        verbose_name = 'ORDEN COMPRA'
        verbose_name_plural = 'ORDENES COMPRA'