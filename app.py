from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

# Simulamos una base de datos con una lista
usuarios = []

class Usuario(Resource):
    def get(self, id=None):
        if id is None:
            return usuarios
        for usuario in usuarios:
            if usuario['id'] == id:
                return usuario
        return {"message": "Usuario no encontrado"}, 404

    def post(self):
        nuevo_usuario = {
            "id": len(usuarios) + 1,
            "nombre": request.json['nombre'],
            "apellido": request.json['apellido'],
            "correo": request.json['correo'],
            "direccion": request.json['direccion'],
            "profesion": request.json['profesion']
        }
        usuarios.append(nuevo_usuario)
        return nuevo_usuario, 201

    def put(self, id):
        for usuario in usuarios:
            if usuario['id'] == id:
                usuario.update(request.json)
                return usuario
        return {"message": "Usuario no encontrado"}, 404

    def delete(self, id):
        for index, usuario in enumerate(usuarios):
            if usuario['id'] == id:
                return usuarios.pop(index)
        return {"message": "Usuario no encontrado"}, 404

api.add_resource(Usuario, '/usuario', '/usuario/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)