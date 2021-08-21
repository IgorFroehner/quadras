import datetime as dt
from app import db


class Evento(db.Document):
    titulo = db.StringField(required=True, max_length=20)
    inicio = db.DateTimeField()
    fim = db.DateTimeField()
    blocos = db.ListField(db.StringField())


def select_all():
    return Evento.objects


def insert(evento: Evento):
    evento.save()


def insert_from_dict(_dict: dict):
    inst = from_dict(_dict)
    inst.save()


def from_dict(_dict: dict) -> Evento:
    evento = Evento(
        titulo=_dict['titulo'],
        inicio=dt.datetime.combine(_dict['data_inicio'], _dict['hora_inicio']),
        fim=dt.datetime.combine(_dict['data_fim'], _dict['hora_fim']),
    )
    for nome in _dict['blocos']:
        evento.blocos.append(nome)
    return evento
