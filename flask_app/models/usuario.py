from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('certificacion_1').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('certificacion_1').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('certificacion_1').query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL('certificacion_1').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])