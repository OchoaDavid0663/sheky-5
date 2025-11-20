from django.contrib import admin
from .models import Color, Pedido, Usuario, Personalizado, Pintura, Producto, Sellador


admin.site.register(Sellador)
admin.site.register(Producto)
admin.site.register(Pintura)
admin.site.register(Personalizado)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Color)
