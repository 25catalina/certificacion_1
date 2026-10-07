from flask_app.config.mysqlconnection import connectToMySQL #todas las clases importan mysqlconnection

class Usuario:
    #metodo constructor para usuarios
    def __init__(self, data):
        self.id = data.get('id') #el get es para obtener el valor de la clave 'id' del diccionario data, si no existe, devuelve None
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')

        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

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