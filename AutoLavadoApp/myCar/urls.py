from django.contrib import admin
from django.urls import path, include
#permite indicar que la ubicacion es estatica
from django.conf.urls.static import static
#debemos importar el archivo "setting" (variales MEDIA)
from django.conf import settings
from .views import index,galeria,formulario,local,insumos,login,logout_vista,admin_insumos,eliminar,actualizar_insumos,actualiza
urlpatterns = [
    path('',index, name='IND'),
    path('galeria/',galeria,name='GAL'),
    path('formulario/',formulario,name='FORM'),
    path('local/',local,name='LOC'),
    path('insumos/',insumos,name='INS'),
    path('login/',login,name='LOGIN'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('admin_insumos/',admin_insumos,name='ADM'),
    path('eliminar/<id>/',eliminar,name='ELIM'),
    path('actualizar_insumos/<id>/',actualizar_insumos,name='ACT'),
    path('actualiza/',actualiza,name='ACTMAS'),
]

admin.site.site_header="Administracion Autolavado Miguel"
admin.site.index_title="Modulo Administrativo"
admin.site.site_title="Autolavado Mi Pana Miguel" 