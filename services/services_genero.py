from database.models import Genero
from database import db

def post_genero(data):
    if not data:
        return None
    if data.get("nombre") is None:
        return None
    nuevo_genero = Genero(nombre = data["nombre"])
    db.session.add(nuevo_genero)
    db.session.commit()
    return nuevo_genero.to_dict()

def get_genero(id):
    genero = Genero.query.get(id)
    if not genero:
        return None
    return genero.to_dict()

def get_generos():
    generos = Genero.query.all()
    return [genero.to_dict() for genero in generos]

def patch_genero(id, data):
    if not data:
        return None
    genero = Genero.query.get(id)
    if not genero:
        return None
    if "nombre" in data and data["nombre"] is not None:
        setattr(genero, "nombre", data["nombre"])
        db.session.commit()
        return genero.to_dict()

def delete_genero(id):
    genero = Genero.query.get(id)
    if not genero:
        return False
    else:
        db.session.delete(genero)
        db.session.commit()
    return True
    

    