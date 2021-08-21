from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired

from model import bloco_dao


class EventoForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    data_inicio = DateField('Data Início', validators=[DataRequired()])
    hora_inicio = TimeField('Hora Início', validators=[DataRequired()])
    data_fim = DateField('Data Fim', validators=[DataRequired()])
    hora_fim = TimeField('Hora Fim', validators=[DataRequired()])
    blocos = SelectMultipleField('Blocos', validators=[DataRequired()])

    def __init__(self):
        super(EventoForm, self).__init__()
        self.blocos.choices = [(bloco.id_bloco, bloco.id_bloco) for bloco in bloco_dao.select_all()]

