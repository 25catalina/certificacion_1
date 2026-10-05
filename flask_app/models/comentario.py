from flask_app.config.mysqlconnection import connectToMySQL

class Comentario:
    def __init__(self, data):
        self.id = data['id']
        self.comentario = data['comentario']
        self.usuario_id = data['usuario_id']
        self.pelicula_id = data['pelicula_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO comentarios (comentario, usuario_id, pelicula_id, created_at, updated_at) VALUES (%(comentario)s, %(usuario_id)s, %(pelicula_id)s, NOW(), NOW());"
        return connectToMySQL('certificacion_1').query_db(query, data)