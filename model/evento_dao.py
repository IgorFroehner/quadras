from app import db


class Evento(db.Model):
    id_evento = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)


def select_all():
    # TODO: fazer retornar os blocos que o evento vai ocorrer
    return db.session.query(Evento.id_evento, Evento.titulo, Evento.data_inicio, Evento.hora_inicio, Evento.data_fim,
                            Evento.hora_fim) \
        .all()


def select_next_id() -> int:
    f = db.func.nextval('evento_id_evento_seq')
    return db.session.query(f).first()[0]


def insert(evento: Evento):
    db.session.add(evento)
    db.session.commit()


def insert_from_dict(_dict: dict):
    inst = from_dict(_dict)
    insert(inst)


def from_dict(_dict: dict) -> Evento:
    return Evento(
        id_evento=(_dict['id_evento'] if 'id_evento' in _dict else None),
        titulo=_dict['titulo'],
        data_inicio=_dict['data_inicio'],
        data_fim=_dict['data_fim'],
        hora_inicio=_dict['hora_inicio'],
        hora_fim=_dict['hora_fim'],
    )
