from django.db import models

# Create your models here.

class Insumos(models.Model):
    nombre = models.CharField (max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=300)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre
#MODELOS DE COMPONENTES DE GALERIA
class Imagen_emp(models.Model):
    nombre = models.CharField(max_length=60,primary_key=True)
    imagen = models.ImageField(upload_to='empleados',null=False)
    
    def __str__(self):
        return self.nombre
        
class Slider(models.Model):
    nombre = models.CharField(max_length=60, primary_key=True)
    Imagen = models.ImageField(upload_to='slider',null=False)

    def __str__(self):
        return self.nombre
#MODELOS DE COMPONENTES DE GALERIA
class MisionVision(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    vision = models.CharField(max_length=400)
    mision = models.CharField(max_length=400)

    def __str__(self):
        return self.ident

class sliderindex(models.Model):
    nombre = models.CharField(max_length=60, primary_key=True)
    descripcion = models.TextField(max_length=200)
    Imagen = models.ImageField(upload_to='sliderindex',null=False)

    def __str__(self):
        return self.nombre