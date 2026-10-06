from flask_app.config.mysqlconnection import connectToMySQL

class Pelicula:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.director = data['director']
        self.sinopsis = data['sinopsis']
        self.created_at = data['created_at']
        self.fecha_estreno = data['fecha_estreno']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO peliculas (nombre, director, sinopsis, created_at, fecha_estreno, updated_at, usuario_id) VALUES (%(nombre)s, %(director)s, %(sinopsis)s, NOW(), %(fecha_estreno)s, NOW(), %(usuario_id)s);"
        return connectToMySQL('certificacion_1').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM peliculas;"
        results = connectToMySQL('certificacion_1').query_db(query)
        peliculas = []
        for pelicula in results:
            peliculas.append(cls(pelicula))
        return peliculas

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM peliculas WHERE id = %(id)s;"
        result = connectToMySQL('certificacion_1').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod
    def update(cls, data):
        query = "UPDATE peliculas SET nombre = %(nombre)s, director = %(director)s, sinopsis = %(sinopsis)s, fecha_estreno = %(fecha_estreno)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('certificacion_1').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM peliculas WHERE id = %(id)s;"
        return connectToMySQL('certificacion_1').query_db(query, data)