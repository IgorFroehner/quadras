
from app import db


class Esporte(db.Model):
    id_esporte = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))


def select_next_id() -> int:
    f = db.func.nextval('esporte_id_esporte_seq')
    return db.session.query(f).first()[0]


def select_all():
    return db.session.query(Esporte.id_esporte, Esporte.nome).all()


def insert(esporte: Esporte):
    db.session.add(esporte)
    db.session.commit()


def insert_from_dict(dict_esporte: dict):
    esporte = from_dict(dict_esporte)
    insert(esporte)


def from_dict(_dict: dict) -> Esporte:
    return Esporte(
        id_esporte=(_dict['id_esporte'] if 'id_esporte' in _dict else None),
        nome=_dict['nome']
    )
