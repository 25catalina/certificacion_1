from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.comentario import Comentario

@app.route("/crear_comentario", methods=["POST"])
def crear_comentario():
    comentarios = Comentario.get_all()
    return render_template("ver_pelicula.html", comentarios=comentarios)

@app.route("/guardar_comentario", methods=["POST"])
def guardar_comentario():
    data = {
        "comentario": request.form['comentario'],
        "usuario_id": session['usuario_id'],
        "pelicula_id": request.form['pelicula_id']
    }
    Comentario.save(data)
    return redirect(f"/crear_comentario/{request.form['pelicula_id']}")