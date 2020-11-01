from django.test import TestCase
import unittest
from .models import MisionVision,Insumos,Imagen_emp,Slider,Slider,sliderindex

# Create your tests here.
class TestUno(unittest.TestCase):

    def test_igualdad_cadenas(self):
        self.assertEqual('ii','ii')

    def test_texto_mayuscula(self):
        self.assertEqual('ii' .upper(),'II')

    def test_no_esta_el_contenido(self):
        self.assertFalse('hola ' in 'es un HOLA mundo')
        
    def grabar_imagen(self):
        image = Imagen_emp(
            nombre="foto1", imagen="imagen1.jpg"
        )
        valor=0
        try:
            image.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)
        
    def grabar_slider(self):
        sli = Slider(
            nombre="slider", Imagen="slider1.jpg"
        )
        valor=0
        try:
            sli.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)
        
    def grabar_sliderindex(self):
        slindex = sliderindex(
            nombre="slider",descripcion"Lo mejor en autolavados!" ,Imagen="cliente1.jpg"
        )
        valor=0
        try:
            slindex.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)

    def grabar_misionvision(self):
        m = MisionVision(
            ident="dos", mision="nuestra mision es..." ,vision="nuestra vision es..."
        )
        valor=0
        try:
            m.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)
        
    def grabar_insumo(self):
        insumo = Insumos.objects.get( nombre="wd40")
        valor=0
        try:
            insumo.delete()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)
        
    def eliminar_insumo(self):
        insumo = Insumos( nombre="wd40",precio="1500",descripcion="lubricante",stock="20"
        )
        valor=0
        try:
            insumo.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)
        
    def lista_myv(self):
        ins= Insumos.objects.all()
        self.assertIsInstance(ins,Insumos)  
        
    def lista_myv(self):
        lm= MisionVision.objects.all()
        self.assertIsInstance(lm,MisionVision)   

        
if __name__ == "__main__":
    unittest.main()