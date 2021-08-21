
from app import db


class Bolsista(db.Document):
    cpf = db.StringField(required=True, max_length=20)

