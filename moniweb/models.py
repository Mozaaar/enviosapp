from django.db import models

# Create your models here.
class Departamento(models.Model):
    id_departamento = models.CharField(max_length=10, primary_key=True)  # Clave primaria
    nombre = models.CharField(max_length=100)
class Ciudad(models.Model):
    id_ciudad = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
class Sede(models.Model):
    id_sede = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

class TipoTransporte(models.Model):
    id_tipo_transporte = models.CharField(max_length=10, primary_key=True)
    transporte = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

class Transportista(models.Model):
    id_transportista = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    id_tipo_transporte = models.ForeignKey(TipoTransporte, on_delete=models.CASCADE)

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

class Producto(models.Model):
    id_producto = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()

class Pedido(models.Model):
    id_pedido = models.CharField(max_length=10, primary_key=True)
    fecha = models.DateField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Envio(models.Model):
    id_envio = models.CharField(max_length=10, primary_key=True)
    direccion_destino = models.CharField(max_length=255)
    fecha_envio = models.DateField()
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    id_sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

class Paquete(models.Model):
    id_paquete = models.CharField(max_length=10, primary_key=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    dimensiones = models.CharField(max_length=100)
    contenido = models.TextField()
    id_envio = models.ForeignKey(Envio, on_delete=models.CASCADE)

class Factura(models.Model):
    id_factura = models.CharField(max_length=10, primary_key=True)
    fecha_emision = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

class Pago(models.Model):
    id_pago = models.CharField(max_length=10, primary_key=True)
    tipo_pago = models.CharField(max_length=10, choices=[('credito', 'Credito'), ('efectivo', 'Efectivo')])
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    hora = models.TimeField()
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class PedPro(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_pedido', 'id_producto'),)

class PaquPro(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_producto', 'id_paquete'),)