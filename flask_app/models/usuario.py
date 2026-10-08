from flask_app.config.mysqlconnection import connectToMySQL #todas las clases importan mysqlconnection

import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')


#metodo constructor para usuarios
class Usuario:
    def __init__(self, data):
        self.id = data.get('id') #el get es para obtener el valor de la clave 'id' del diccionario data, si no existe, devuelve None
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')

        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')# Objeto de expresión regular que usaremos para validar
        

         

    
    #metodo de clase para guardar un registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('certificacion_1').query_db(query, data)
    #dentro de los () se pone el nombre de la base de datos


    #metodo ver todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuarios_en_db = connectToMySQL('certificacion_1').query_db(query)
        usuarios = []

        #por cada usuario en db, voy a crear una instancia de la clase Usuario
        for usuario in usuarios_en_db:
            usuarios.append(cls(usuario))
            #append agrega un elemento en la lista usuarios
        return usuarios
    
    
    #metodo para ver 1 registro
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        usuarios_en_db = connectToMySQL('certificacion_1').query_db(query, data)
        return cls(usuarios_en_db[0])

    
    #metodo para editar registro
    @classmethod
    def update(cls, data):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, password = %(password)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('certificacion_1').query_db(query, data)

    #metodo para eliminar registro
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('certificacion_1').query_db(query, data)

    @classmethod 
    def get_by_email(cls, data):
         query = "SELECT * FROM usuarios WHERE email = %(email)s;"
         usuarios_en_db = connectToMySQL('certificacion_1').query_db(query, data)
         return cls(usuarios_en_db[0])
                

#usamos metodo estatico para validar los formularios
    @staticmethod
    def validar_usuario( usuario ):
         es_valido = True#por cada validacion que yo haga, voy a un if 
         #Revisa si el campo coincide con el patrón
         if not EMAIL_REGEX.match(usuario['email']):
            flash("E-mail inválido")
            es_valido = False

         if len(usuario['nombre']) < 2:
            flash("Nombre de usuario necesita al menos 2 caracteres", "usuario")
            es_valido= False

         if len(usuario['apellido']) < 2:
                       flash("El apellido del usuario necesita al menos 2 caracteres", "usuario")
                       es_valido= False
                       #falta validacion de contraseña = confirmacion contraseña
                       
         if not usuario['password'] == usuario['password_conf']:
            flash('La contraseña no coindice con la confirmacion')
            es_valido= False

         if not Usuario.get_by_email ("email".usuario ["email"]):
            flash ("el correo no se encuentra")
            es_valido = False
            return es_valido

    @staticmethod
    def validar_login (Usuario):
         if not Usuario.get_by_email ("email".usuario ["email"]):
                     flash ("el correo no se encuentra en la base de datos")
                     es_valido = False
                     return es_valido