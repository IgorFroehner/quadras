
from app import db


class Bloco(db.Document):
    id_bloco = db.StringField(required=True, max_length=10)


def select_all():
    return Bloco.objects


def find(params: dict):
    return Bloco.objects(__raw__=params).first()


def insert(bloco: Bloco):
    db.session.add(bloco)
    db.session.commit()


def insert_from_dict(_dict: dict):
    inst = from_dict(_dict)
    inst.save()


def from_dict(_dict: dict) -> Bloco:
    return Bloco(
        id_bloco=_dict['id_bloco']
    )
