
from app import db


class Bolsista(db.Model):
    __tablename__ = 'quadra'
    cpf = db.Column(db.String, db.ForeignKey('usuario.cpf'))


def select_next_id() -> int:
    # TODO: arrumar isso aqui pra retornar a sequencia de bolsista
    f = db.func.nextval('esporte_id_esporte_seq')
    return db.session.query(f).first()[0]
