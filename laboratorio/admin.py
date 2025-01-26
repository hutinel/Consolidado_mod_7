from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.


class laboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('nombre', 'laboratorio')
    list_fields = ('nombre', 'laboratorio__nombre')    

admin.site.register(Laboratorio, laboratorioAdmin) 
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)


