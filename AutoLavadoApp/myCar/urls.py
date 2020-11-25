from django.contrib import admin
from django.urls import path, include
#permite indicar que la ubicacion es estatica
from django.conf.urls.static import static
#debemos importar el archivo "setting" (variales MEDIA)
from django.conf import settings
from .views import index,galeria,formulario,local,insumos,login,logout_vista,admin_insumos,eliminar,actualizar_insumos,actualiza,listar_por_precio_api,listar_por_nombre_api,guardar_token,contacto

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
    path('listar_precio_api/',listar_por_precio_api,name='LPA'),
    path('listar_nombre_api/',listar_por_nombre_api,name='LNA'),
    # APP FACEBOOK
    path('oauth/', include('social_django.urls', namespace='social')),
    path('guardar-token/',guardar_token,name='guardar-token'),

]

admin.site.site_header="Administracion Autolavado Miguel"
admin.site.index_title="Modulo Administrativo"
admin.site.site_title="Autolavado Mi Pana Miguel" 