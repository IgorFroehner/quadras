from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class BlocoForm(FlaskForm):
    id_bloco = StringField('Identificador do Bloco', validators=[DataRequired()])

