
from app import db


class Usuario(db.Document):
    cpf = db.StringFiedl(required=True)
    email = db.EmailField(required=True)
    senha = db.StringField(required=True)
    permissao = db.StringField(15)
