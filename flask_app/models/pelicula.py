from flask_app.config.mysqlconnection import connectToMySQL


#metodo constructor
class Pelicula:
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.director = data.get('director')
        self.sinopsis = data.get('sinopsis')
        self.created_at = data.get('created_at')
        self.fecha_estreno = data.get('fecha_estreno')
        self.updated_at = data.get('updated_at')
        self.usuario_id = data.get('usuario_id')


        
    #metodo para guardar un registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO peliculas (nombre, director, sinopsis, created_at, fecha_estreno, updated_at, usuario_id) VALUES (%(nombre)s, %(director)s, %(sinopsis)s, NOW(), %(fecha_estreno)s, NOW(), %(usuario_id)s);"
        return connectToMySQL('certificacion_1').query_db(query, data)

    
    
    #metodo para obtener todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM peliculas;"
        peliculas_en_db = connectToMySQL('certificacion_1').query_db(query)
        peliculas = []
        for pelicula in peliculas_en_db:
            peliculas.append(cls(pelicula))
        return peliculas

    
    
    #metodo para ver 1 registro
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM peliculas WHERE id = %(id)s;"
        peliculas_en_db = connectToMySQL('certificacion_1').query_db(query, data)
        return cls(peliculas_en_db[0])
    
    
    #metodo para editar registro
    @classmethod
    def update(cls, data):
        query = "UPDATE peliculas SET nombre = %(nombre)s, director = %(director)s, sinopsis = %(sinopsis)s, fecha_estreno = %(fecha_estreno)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('certificacion_1').query_db(query, data)
    
    
    
    #metodo para eliminar registro
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM peliculas WHERE id = %(id)s;"
        return connectToMySQL('certificacion_1').query_db(query, data)