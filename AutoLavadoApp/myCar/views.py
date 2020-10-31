from django.shortcuts import render
from .models import Insumos,Imagen_emp,MisionVision,Slider,sliderindex
#importar la tabla de usuarios desde el administrador
from django.contrib.auth.models import User
#importar librerias de autentificacion
from django.contrib.auth import authenticate,logout,login as loguin_autent
#agregar una decoracion que permite evitar el ingreso a las paginas
#sin estar registrado
from django.contrib.auth.decorators import login_required,permission_required


def logout_vista(request):
    logout(request)
    sindex = sliderindex.objects.all()
    return render(request,'index.html',{'sindex':sindex})  

def login(request):
    if request.POST:
        usuario = request.POST.get("usuario")
        password = request.POST.get("clave")
        us = authenticate(request,username=usuario,password=password)
        if us is not None and us.is_active:
            loguin_autent(request,us)
            sindex = sliderindex.objects.all()
            return render(request,'index.html',{'user':us,'sindex':sindex})  
        else:
            return render(request,'login.html',{'msg':'clave o pass incorrecto'}) 
    return render(request,'login.html')


def index(request):
    sli = sliderindex.objects.all()
    return render(request,'index.html',{'sli':sli})


def galeria(request):
    imagen = Imagen_emp.objects.all()
    slider = Slider.objects.all()
    return render(request,'galeria.html',{'lista_imagenes':imagen,'slider':slider})


def formulario(request):
    if request.POST:
        nomb = request.POST.get("txtnombre")
        ape = request.POST.get("txtapellido")
        correo = request.POST.get("txtcorreo")
        user = request.POST.get("txtuser")
        clave1 = request.POST.get("txtpass")
        clave2 = request.POST.get("txtpass2")
        if clave1!=clave2:
            mensaje="Las contraseñas deben ser iguales!"
            return render(request,'formulario.html',{'msg':mensaje })

        try:
            u=User.objects.get(username=user)
            mensaje="Este usuario ya existe"
            return render(request,'formulario.html',{'msg':mensaje })
        except:
            u =User()
            u.first_name=nomb
            u.last_name=ape
            u.email=correo
            u.username =user
            u.set_password(clave1)
            u.save()
            us = authenticate(request,username=user,password=clave1)
            loguin_autent(request,us)  
            sli = sliderindex.objects.all() 
        return render(request,'index.html',{'user':us,'sli':sli})
    return render(request,'formulario.html',{'msg':''})

@login_required(login_url='/loguin/')
@permission_required('AutoLavadoApp.add_Insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nom = request.POST.get("txtnom")
        pre = request.POST.get("txtprecio")
        desc = request.POST.get("txtdesc")
        sto = request.POST.get("txtstock")
        insum = Insumos(
            nombre = nom,
            precio = pre,
            descripcion = desc,
            stock = sto
        )
        insum.save()
        return render(request,'insumos.html',{'lista_insumos':insumos,'msg':'Insumo agregado'})
    return render(request,'insumos.html',{'lista_insumos':insumos,'msg':'nn'})


def local(request):
    myv = MisionVision.objects.all()
    return render(request,'local.html',{'myv':myv})

@login_required(login_url='/loguin/')
@permission_required('AutoLavadoApp.add_Insumos',login_url='/login/')
@permission_required('AutoLavadoApp.change_Insumos',login_url='/login/')
@permission_required('AutoLavadoApp.delete_Insumos',login_url='/login/')
@permission_required('AutoLavadoApp.view_Insumos',login_url='/login/')
def admin_insumos(request):
    lista_i =Insumos.objects.all()
    return render(request,'admin_insumos.html',{'lista_i':lista_i})

@permission_required('AutoLavadoApp.delete_Insumos',login_url='/login/')
@login_required(login_url='/loguin/')
def eliminar(request,id):
    try:
        ins = Insumos.objects.get(nombre=id) 
        ins.delete()
        mensaje='Insumo eliminado'  
    except:
        mensaje='Insumo inexistente'
    insumos=Insumos.objects.all()
    return render(request,'admin_insumos.html',{'msg':mensaje,'lista_i':insumos,'msg':mensaje})

@login_required(login_url='/loguin/')
@permission_required('AutoLavadoApp.view_Insumos',login_url='/login/')
def actualizar_insumos(request,id):
    insumos=Insumos.objects.all()
    try:
        ins = Insumos.objects.get(nombre=id)
        return render(request,'actualizar_insumos.html',{'ins':ins,'lista_i':insumos})
    except:
        mensaje="Insumo no existente"
    insumos=Insumos.objects.all()
    return render(request,'actualizar_insumos.html',{'msg':mensaje,'lista_i':insumos})

@permission_required('AutoLavadoApp.view_Insumos',login_url='/login/')
@permission_required('AutoLavadoApp.change_Insumos',login_url='/login/')
@login_required(login_url='/loguin/')
def actualiza(request):
    if request.POST:
        nom = request.POST.get("txtnom")
        pre = request.POST.get("txtprecio")
        desc = request.POST.get("txtdesc")
        sto = request.POST.get("txtstock")
        try:
            ins =Insumos.objects.get(nombre=nom)
            ins.precio=pre
            ins.descripcion=desc
            ins.stock=sto
            ins.save()
            mensaje="Insumo Actualizado"
        except:
            mensaje="Insumo no encontrado"

    lista_insumos =Insumos.objects.all() 
    return render(request,'admin_insumos.html',{'msg':mensaje,'lista_i':lista_insumos})