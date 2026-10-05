from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.usuario import Usuario
from flask_app.models.pelicula import Pelicula

@app.route("/")
def inicio():
    return redirect("/usuarios")

@app.route("/usuarios")
def usuarios_page():
    usuarios = Usuario.get_all()
    return render_template("registro.html", usuarios=usuarios)

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],   
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": request.form["password"]
    }
    Usuario.save(data)
    return redirect("/pelicula")


@app.route('/mostrar_usuario/<int:usuario_id>')
def detalle_usuario(usuario_id):
    datos = {
        'id': usuario_id
    }
    usuario = Usuario.get_one(datos)
    return render_template("cine.html",usuario = usuario)


@app.route("/login", methods=["POST"])
def login():
    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    Usuario.save(data)
    usuario = Usuario.get_by_email(data)
    if usuario:
        session["usuario_id"] = usuario.id
        return redirect("/pelicula")
    else:
        flash("Credenciales inválidas", "login")
        return redirect("/usuarios")


