from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash, redirect


#importamos la clase que estamos controlando

from flask_app.models.usuario import Usuario

@app.route("/")
def inicio():
    return redirect("/usuarios")

@app.route("/usuarios")
def usuarios_page():
    usuarios = Usuario.get_all()
    return render_template("registro.html", usuarios=usuarios)


#registro / crear usuario
@app.route('/crear_usuario', methods= ["POST"])
def crear_usuario():

    #para agregar un usuario lo primero que debo hacer es
    #recuperar la informacion desde el formulario
    #para hacer eso necesitamos el request.form
    #%(nombre)s, %(apellido)s, %(email)s,%(password)s

    #--- IMPORTANTE: TEORICAMENTE ANTES DE REGISTRAR UN NUEVO DATO
    #--- YO DEBERÍA VALIDAR QUE LOS DATOS INGRESADOS
    #--- SEAN VALIDOS

    if not Usuario.validar_usuario(request.form):
        
        return redirect('/')

    #--- VALIDACIONES ---

    datos_usuario_registro= {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
         'password':request.form['password']
    }
    
    return ''

#inicio sesión 


#cerrar sesión


@app.route('/crear_usuario', methods=['POST'])
def registrar():
   datos_usuario_registro = {
        "nombre": request.form["nombre"], #debe tener el mismo nombre del name en el formulario
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": request.form["password"], 
        "confirm_password": request.form["confirm_password"]
    }
   resultado = Usuario.save(datos_usuario_registro)
   session['usuario_id'] = resultado

   if not Usuario.validar_usuario(request.form):
       # redirigimos a la plantilla con el formulario
       return redirect('/')
   # ... más código... guardamos
   flash("El correo es obligatorio", "correo") #La categoría es "correo"
   return redirect('/pelicula')



@app.route('/mostrar_usuario/<int:usuario_id>')
def detalle_usuario(usuario_id):
    datos = {
        'id': usuario_id
    }
    usuario = Usuario.get_one(datos)
    return render_template("cine.html",usuario = usuario)

@app.route("/iniciar_sesion", methods=["POST"])
def login():
    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    usuario = Usuario.get_by_email(data)
    if not usuario: #dice si el usuario no existe; se mandara un mensaje
        flash("Correo electrónico no encontrado", "login") 
        #el flash es para mandar un mensaje de error
    if usuario.password != data["password"]: #dice si el password esta malo, te manda un mensaje
        flash("Contraseña incorrecta", "login")
        return redirect("/usuarios")
    session['usuario_id'] = usuario.id 
    #session es para guardar el id del usuario al iniciar sesion, para que no tenga que volver a iniciar sesion
    return redirect("/pelicula")

#retroalimentacion 1
@app.route("/logout") #el logout es para cerrar sesion, se borra la session del usuario
def logout():
    session.clear() #borra la session del usuario
    return redirect("/usuarios")