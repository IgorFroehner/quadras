
from app import db


class Quadra(db.Document):
    largura = db.FloatField(required=True)
    comprimento = db.FloatField(required=True)
    bloco = db.ReferenceField('Bloco', required=True)
    esportes = db.ListField(db.StringField())


def select_all():
    return Quadra.objects


def find_esportes(id_quadra: str):
    quadra = Quadra.objects(id=id_quadra).first()
    esportes = quadra.esportes
    return esportes


def find(params: dict):
    return Quadra.objects(__raw__=params).first()


def find_by_id(id: str):
    return Quadra.objects.get(id=id)


def insert(quadra: Quadra):
    quadra.save()


def insert_from_dict(_dict: dict):
    inst = from_dict(_dict)
    inst.save()


def from_dict(_dict: dict) -> Quadra:
    from model import bloco_dao

    quadra = Quadra(
        largura=_dict['largura'],
        comprimento=_dict['comprimento'],
        bloco=bloco_dao.find({'id_bloco': _dict['bloco']})
    )
    for nome in _dict['esportes']:
        quadra.esportes.append(nome)
    return quadra
