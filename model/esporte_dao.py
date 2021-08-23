
from app import db


class Esporte(db.Document):
    nome = db.StringField(required=True, max_length=20)


def select_all():
    return Esporte.objects


def find(params: dict):
    return Esporte.objects(__raw__=params).first()


def insert(esporte: Esporte):
    esporte.save()


def insert_from_dict(dict_esporte: dict):
    esporte = from_dict(dict_esporte)
    esporte.save()


def from_dict(_dict: dict) -> Esporte:
    return Esporte(
        nome=_dict['nome']
    )
