from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(DetallePedido)


