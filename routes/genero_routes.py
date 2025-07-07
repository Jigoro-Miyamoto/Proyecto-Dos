from flask import Blueprint, request, jsonify
import services.services_genero as sg

genero_bp = Blueprint("genero_api", __name__)

@genero_bp.route("", methods = ["POST"])
def post_gener_r():
    data = request.get_json()
    nuevo_genero = sg.post_genero(data)
    if not nuevo_genero:
        return jsonify({"message": "Error al añadir nuevo genero"})
    return jsonify(nuevo_genero)

@genero_bp.route("", methods = ["GET"])
def get_generos_r():
    generos = sg.get_generos()
    return jsonify(generos)

@genero_bp.route("/<int:id>", methods = ["GET"])

def get_genero_r(id):
    genero = sg.get_genero()
    if not genero:
        return jsonify({"Message":f"No se ha encontrado el genero de ID:{id}"}), 404
    return jsonify(genero)
@genero_bp.route("/<int:id>", methods = ["PATCH"])

def patch_genero_r(id):
    data = request.get_json()
    if not data:
        return jsonify({"message": "Error, ingrese datos para actualizar"})
    genero = sg.patch_genero(id, data)
    if not genero:
        return jsonify({"Message":f"No se ha encontrado el genero de ID:{id}"}), 404
    return jsonify(genero)
    
@genero_bp.route("/<int:id>", methods = ["DELETE"])

def delete_juego_route(id):
    genero = sg.delete_genero(id)
    if not genero:
        return jsonify({"message":f"No se encontro el juego de id {id}"}), 404
    else:
        return jsonify({"message": "El juego se ha borrado exitosamente"}), 204

