from django.contrib import admin
from .models import *

class CatProdAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(CatProduct, CatProdAdmin)
admin.site.register(Producto, ProductAdmin)
