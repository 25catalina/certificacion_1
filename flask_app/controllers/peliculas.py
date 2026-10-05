from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.usuario import Usuario
from flask_app.models.pelicula import Pelicula


@app.route("/pelicula", methods=["GET"])
def nueva_pelicula():
    return render_template("cine.html")


@app.route("/crear_pelicula", methods=["POST"])
def crear_pelicula():
    return render_template("crear_pelicula.html")


@app.route('/guardar_pelicula', methods=["POST, GET"])
def guardar_pelicula():
    data = {
        "nombre": request.form['nombre'],
        "director": request.form['director'],
        "fecha_estreno": request.form['created_at'],
        "sipnosis": request.form['sipnosis'],
    }
    Pelicula.save(data)
    return redirect("/pelicula")


@app.route("/mostrar_pelicula")
def mostrar_pelicula():
    peliculas = Pelicula.get_all()
    return redirect("/ver_pelicula", peliculas=peliculas)

@app.route("/ver_pelicula/<int:id>")
def ver_pelicula(id):
    datos = {
        "id": id
    }
    pelicula = Pelicula.get_one(datos)
    return render_template("cine.html", pelicula=pelicula)


@app.route("/actualizar_pelicula/<int:id>", methods=["GET"])
def editar_pelicula(id):
    data = {
        "id": id
    }
    pelicula = Pelicula.get_one(data)
    return render_template("editar.html", pelicula=pelicula)

@app.route("/eliminar_pelicula/<int:id>", methods=["POST"])
def eliminar_pelicula(id):
    data = {
        "id": id
    }
    Pelicula.delete(data)
    return redirect("/pelicula")