from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models import usuario
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


@app.route("/login", methods=["POST"])
def login():
    datos = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    usuario = Usuario.get_by_email(datos)
    if not usuario:
        flash("Email no registrado", "login")
        return redirect("/usuarios")

