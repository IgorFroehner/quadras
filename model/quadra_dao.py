import sqlalchemy.exc

from app import db


quadra_esporte = db.Table('quadra_esporte',
                          db.Column('id_quadra', db.Integer, db.ForeignKey('quadra.id_quadra'), primary_key=True),
                          db.Column('id_esporte', db.Integer, db.ForeignKey('esporte.id_esporte'), primary_key=True))


class Quadra(db.Model):
    __tablename__ = 'quadra'
    id_quadra = db.Column(db.Integer, primary_key=True)
    largura = db.Column(db.Float, nullable=False)
    comprimento = db.Column(db.Float, nullable=False)
    id_bloco = db.Column(db.Integer, db.ForeignKey('bloco.id_bloco'), nullable=False)
    esportes = db.relationship('Esporte', secondary=quadra_esporte, lazy='subquery',
                               backref=db.backref('esporte', lazy=True))


def select_all():
    from model import Bloco

    return db.session.query(Quadra.id_quadra, Quadra.comprimento, Quadra.largura, Bloco.id_bloco) \
        .join(Bloco, Bloco.id_bloco == Quadra.id_bloco) \
        .all()


def select_next_id() -> int:
    f = db.func.nextval('quadra_id_quadra_seq')
    return db.session.query(f).first()[0]


def insert(quadra: Quadra):
    db.session.add(quadra)
    db.session.commit()


def insert_from_dict(_dict: dict):
    inst = from_dict(_dict)
    insert(inst)


def from_dict(_dict: dict) -> Quadra:
    from model import Esporte

    quadra = Quadra(
        id_quadra=(_dict['id_quadra'] if 'id_quadra' in _dict else None),
        largura=_dict['largura'],
        comprimento=_dict['comprimento'],
        id_bloco=_dict['bloco']
    )
    for id_esporte in _dict['esportes']:
        quadra.esportes.append(Esporte(id_esporte=id_esporte))
    return quadra
