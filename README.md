<h1>Informe de casos de pruebas</h1>

<p>Nuestro equipo a tomado la decision de generar los casos de pruebas que se presenteran a continuacion, con el objetivo,
de comprobar el correcto funcionamiento de los requerimiento funcionales requeridos con el cliente y de este modo,asegurar
que se cumple con las exigencias señaladas.</p>

<h1>ID=01</h1> <h1>NOMBRE=Ingresar imagen a galeria</h1> <h1>Datos=foto 1 / archivo imagen1.jpg </h1>
<p>Resultado esperado: El admin de Django permite el ingreso de un nombre de imagen y el respectivo archivo jpg,reflejando
la insercion del archivo en la galeria de la pagina web.</p>

<p>Resultado obtenido= La imagen se genera de manera exitosa en la galeria de imagenes.</p>
codigo:
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
--------------------------------------------------------------------------------------------------
<h1>ID=02</h1> <h1>NOMBRE=Ingresar imagen a slider de galeria</h1> <h1>Datos=slider1 / archivo slider1.jpg </h1>
<p>Resultado esperado: El admin de Django permite el ingreso de un nombre de imagen y el respectivo archivo jpg,reflejando
la insercion del archivo en el slider de la galeria en la pagina web.</p>

<p>Resultado obtenido= La imagen se genera de manera exitosa en el slider de la galeria de imagenes.</p>
codigo:
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
-------------------------------------------------------------------------------------------------
<h1>ID=03</h1> <h1>NOMBRE=Ingresar comentario de cliente en slider de index</h1> <h1>Datos=Brayan Fernandez / archivo cliente1.jpg / Lo mejor en autolavados! </h1>
<p>Resultado esperado: El admin de Django permite el ingreso de un nombre de cliente , su imagen y el comentario,reflejando
la insercion del cliente en la slider de la pagina principal.</p>

<p>Resultado obtenido= La slider se genera de manera exitosa en la mostrando al cliente en cuestion.</p>
codigo:
def grabar_sliderindex(self):
        slindex = sliderindex
            nombre="slider",descripcion"Lo mejor en autolavados!" ,Imagen="cliente1.jpg"
        )
        valor=0
        try:
            slindex.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)
-------------------------------------------------------------------------------------------------
<h1>ID=04</h1> <h1>NOMBRE=Ingresar insumo</h1> <h1>Datos=wd40 / 1500 / lubricante / 20  / </h1>
<p>Resultado esperado: El formulario de ingreso de insumos permite el ingreso de un insumo y todos sus campos,
reflejando este nuevo elemento en la BD y en el administrador de insumos.</p>

<p>Resultado obtenido= La insumo fue agregado de manera exitosa y re refleja en el admin de insumos y en la base de datos .</p>
codigo:
    def grabar_insumo(self):
        insumo = Insumo( nombre="wd40",precio="1500",descripcion="lubricante",stock="20"
        )
        valor=0
        try:
            insumo.save()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)
--------------------------------------------------------------------------------------------
<h1>ID=05</h1> <h1>NOMBRE=Listar insumo</h1>  <h1>Datos=wd40 / 1500 / lubricante / 20  / </h1>
<p>Resultado esperado: El administrador de insumos lista todos los insumos disponibles junto con sus datos.</p>

<p>Resultado obtenido= La lista de insumo se genera de manera exitosa y lista todos los objetos.</p>
codigo:
def lista_myv(self):
        ins= Insumos.objects.all()
        self.assertIsInstance(ins,Insumos)  
--------------------------------------------------------------------------------------------
<h1>ID=06</h1>  <h1>NOMBRE=Eliminar insumo</h1>  <h1>Datos=wd40 / 1500 / lubricante / 20  / </h1>  
<p>Resultado esperado: El administrar de  insumos permite eliminar un insumo, mostrando un mensaje de alerta con el nombre del
insumo antes de su eliminacion.</p>

<p>Resultado obtenido= La insumo fue eliminado de manera correcta, reflejando el efecto en el admin de insumos y la base de datos,
ademas, el nombre del insumo y la alerta fueron presentados antes de su eliminacion.</p>
codigo:
 def grabar_insumo(self):
        insumo = Insumos.objects.get( nombre="wd40")
        valor=0
        try:
            insumo.delete()
            valor=1
        except:
            valor=0
        self.assertEqual(valor,1)

--------------------------------------------------------------------------------------------
<h1>ID=7</h1>   <h1>NOMBRE=agregar mision y vision </h1>  <h1>Datos= ident:dow mision:nuestra mision es .... / vision:nuestra vision es .....</h1>  
<p>Resultado esperado: El admin de Django permite la modificacion de la mision y la vision , reflenjando los cambion en la pagina de 
quienes somos y presentandola por pantalla.</p>

<p>Resultado obtenido= El admin de Django permitio la modificacion de los campos reflejandolos en la pagina de quienes somos.</p>
codigo:
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
