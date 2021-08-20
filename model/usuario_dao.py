
from app import db


class Usuario(db.Model):
    cpf = db.Column(db.String(11), primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    permissao = db.Column(db.String(15))
