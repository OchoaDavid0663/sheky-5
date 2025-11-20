from django.db import models

class Sellador(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Sellador"
        verbose_name_plural = "Selladores"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Pintura(models.Model):
    nombre = models.CharField(max_length=100)
    foto_producto = models.ImageField(upload_to='img_productos/', blank=True, null=True)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Pintura"
        verbose_name_plural = "Pinturas"
        

class Personalizado(models.Model):
    pintura = models.ForeignKey(Pintura, on_delete=models.CASCADE, related_name='personalizados')
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.pintura} : {self.color}"

    class Meta:
        verbose_name = "Personalizado"
        verbose_name_plural = "Personalizados"


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=30)
    pais = models.CharField(max_length=30, choices=[
        ('MEXICO', 'Mexico'),
        ('ESTADOS UNIDOS', 'Estados Unidos'),
        ('GUATEMALA', 'Guatemala'),
        ('EL SALVADOR', 'El Salvador'),
        ('HONDURAS', 'Honduras'),
        ('COSTA RICA', 'Costa Rica'),
        ('PANAMA', 'Panama'),
    ])
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    calle = models.CharField(max_length=50)
    num_domicilio = models.CharField(max_length=10)
    detalles = models.CharField(max_length=250, default='INFORMACION DEL DOMICILIO')

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    productos = models.ManyToManyField(Producto, related_name='pedidos')
    selladores = models.ManyToManyField(Sellador, related_name='pedidos')
    personalizados = models.ManyToManyField(Personalizado, related_name='pedidos')
    metodo_pago = models.CharField(max_length=30, choices=[
        ('TARJETA', 'Tarjeta'),
        ('MERCADO PAGO', 'Mercado Pago'),
        ('OXXO', 'Oxxo'),
    ])
    total = models.DecimalField(max_digits=20, decimal_places=2)
    fecha = models.DateField()
    
    def __str__(self):
        return f"{self.usuario} - ${self.total}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class Color(models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    tipo = models.CharField(max_length=30, choices=[
        ('CALIDOS', 'Calidos'),
        ('FRIOS', 'Frios'),
        ('GRISES', 'Grises'),
        ('PASTELES', 'Pasteles'),
        ('VIVOS', 'Vivos'),
    ])
    popularidad = models.IntegerField()

    def __str__(self):
        return f"{self.codigo}"

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colores"
