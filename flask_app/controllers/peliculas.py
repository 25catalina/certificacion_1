from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.usuario import Usuario
from flask_app.models.pelicula import Pelicula

@app.route("/pelicula")
def dashboard():
    if "usuario_id" not in session:
        return redirect("/usuarios")
    peliculas = Pelicula.get_all()
    usuario = Usuario.get_one({"id": session['usuario_id']})
    return render_template("cine.html", peliculas=peliculas, usuario=usuario)


@app.route("/crear_pelicula", methods=["GET"])
def crear_pelicula():
    return render_template("crear_pelicula.html")


@app.route('/guardar_pelicula', methods=["POST"])
def guardar_pelicula():
    data = {
        "nombre": request.form['nombre'],
        "director": request.form['director'],
        
        "sinopsis": request.form['sinopsis'],
        "usuario_id": session['usuario_id'],
        "fecha_estreno": request.form['fecha_estreno']
        }
    Pelicula.save(data)
    return redirect("/pelicula")



@app.route("/editar_pelicula/<int:id>", methods=["POST"])
def actualizar_pelicula(id):
    data = {
        "id": id,
        "nombre": request.form['nombre'],
        "director": request.form['director'],
        "sinopsis": request.form['sinopsis'],
        "fecha_estreno": request.form['fecha_estreno']
    }
    Pelicula.update(data)
    return redirect("/pelicula")


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

@app.route("/ver_pelicula/<int:id>")
def ver_pelicula(id):
    data = {
        "id": id

    }
    pelicula = Pelicula.get_one(data)
    data_usuario = {
        "id": pelicula.usuario_id
    }
    usuario = Usuario.get_one(data_usuario) 
    return render_template("ver_pelicula.html", pelicula=pelicula, usuario= usuario)