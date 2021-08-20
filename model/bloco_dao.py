from app import db


class Bloco(db.Model):
    __tablename__ = 'bloco'
    id_bloco = db.Column(db.String, primary_key=True)


def select_all():
    return db.session.query(Bloco.id_bloco).all()


def select_next_id() -> int:
    f = db.func.nextval('bloco_id_bloco_seq')
    return db.session.query(f).first()[0]


def insert(bloco: Bloco):
    db.session.add(bloco)
    db.session.commit()


def insert_from_dict(_dict: dict):
    inst = from_dict(_dict)
    insert(inst)


def from_dict(_dict: dict) -> Bloco:
    return Bloco(
        id_bloco=_dict['id_bloco']
    )
