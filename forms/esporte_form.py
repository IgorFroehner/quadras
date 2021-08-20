from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

from model import esporte_dao


class EsporteForm(FlaskForm):
    # id_esporte = IntegerField('Id Esporte', validators=[DataRequired()],
    #                           render_kw={'value': f'{esporte_dao.select_next_id()}',
    #                                      'disabled': '', 'readonly': ''})
    nome = StringField('Nome', validators=[DataRequired()])
