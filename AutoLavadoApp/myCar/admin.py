from django.contrib import admin
from .models import Insumos,Imagen_emp,Slider,MisionVision,sliderindex

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['nombre','apellido','email','nombreUser','contrasena']
    search_fields=['nombre','email','nombreUser']
    list_per_page= 10

class InsumosAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','descripcion','stock']
    search_fields=['nombre','precio']
    list_per_page= 10


class Imagen_empAdmin(admin.ModelAdmin):
    list_display=['nombre','imagen']
    search_fields=['nombre']
    list_per_page= 10

class SliderAdmin(admin.ModelAdmin):
    list_display=['nombre']
    search_fields=['nombre']
    list_per_page= 10

class MisionVisionAdmin(admin.ModelAdmin):
    list_display=['ident','mision','vision']
    search_fields=['ident']
    list_per_page= 10

class sliderindexAdmin(admin.ModelAdmin):
    list_display=['nombre','descripcion']
    search_fields=['nombre']
    list_per_page= 10

admin.site.register(Insumos,InsumosAdmin)
admin.site.register(Imagen_emp,Imagen_empAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(MisionVision,MisionVisionAdmin)
admin.site.register(sliderindex,sliderindexAdmin)