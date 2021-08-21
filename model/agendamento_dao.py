import datetime

from app import db


class Agendamento(db.Document):
    data_hora = db.DateTimeField(required=True)
    quadra = db.ReferenceField('Quadra', required=True)
    esporte = db.ReferenceField('Esporte', required=True)


def select_all():
    return Agendamento.objects


def insert(agendamento: Agendamento):
    db.session.add(agendamento)
    db.session.commit()


def insert_from_dict(dict_esporte: dict):
    inst = from_dict(dict_esporte)
    inst.save()


def from_dict(_dict: dict) -> Agendamento:
    from model import esporte_dao, quadra_dao
    print(_dict['quadra'])
    return Agendamento(
        data_hora=datetime.datetime.combine(_dict['date'], _dict['hora']),
        quadra=quadra_dao.find_by_id(_dict['quadra']),
        esporte=esporte_dao.find({'nome': _dict['esporte']})
    )
