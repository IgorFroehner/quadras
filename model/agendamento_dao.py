from app import db


class Agendamento(db.Model):
    id_agendamento = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    hora = db.Column(db.Time)
    id_quadra = db.Column(db.Integer, db.ForeignKey('quadra.id_quadra'))
    id_esporte = db.Column(db.Integer, db.ForeignKey('esporte.id_esporte'))


def select_all():
    from model import Esporte, Quadra
    return db.session.query(Agendamento.id_agendamento, Agendamento.data, Agendamento.hora, Esporte.nome,
                            Quadra.id_bloco, Quadra.id_quadra, Quadra.comprimento, Quadra.largura) \
        .join(Quadra, Quadra.id_quadra == Agendamento.id_quadra) \
        .join(Esporte, Esporte.id_esporte == Agendamento.id_esporte) \
        .all()


def select_next_id() -> int:
    f = db.func.nextval('agendamento_id_agendamento_seq')
    return db.session.query(f).first()[0]


def insert(agendamento: Agendamento):
    db.session.add(agendamento)
    db.session.commit()


def insert_from_dict(dict_esporte: dict):
    inst = from_dict(dict_esporte)
    insert(inst)


def from_dict(_dict: dict) -> Agendamento:
    return Agendamento(
        id_agendamento=(_dict['id_agendamento'] if 'id_agendamento' in _dict else None),
        data=_dict['date'],
        hora=_dict['hora'],
        id_quadra=_dict['quadra'],
        id_esporte=_dict['esporte']
    )
