from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.usuario import Usuario

@app.route("/")
def inicio():
    return redirect("/usuarios")

@app.route("/usuarios")
def usuarios_page():
    usuarios = Usuario.get_all()
    return render_template("registro.html", usuarios=usuarios)


#registro de usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"]
    }
    resultado = Usuario.save(data)
    session['usuario_id'] = resultado
    return redirect("/pelicula")


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