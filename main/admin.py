from django.contrib import admin

# Register your models here.
from .models import *


class ClienteInline(admin.TabularInline):
    model=Cliente

class ColaboradorInline(admin.TabularInline):
    model=Colaborador

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        ColaboradorInline
    ]
admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(DetallePedido)


