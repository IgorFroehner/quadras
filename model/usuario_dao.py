
from app import db


class Usuario(db.Document):
    cpf = db.StringField(required=True)
    email = db.EmailField(required=True)
    senha = db.StringField(required=True)
    permissao = db.StringField()
    authenticated = False

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


def find_by_email(email) -> Usuario:
    return Usuario.objects(email=email).first()
