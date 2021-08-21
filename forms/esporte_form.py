from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired
from flask_mongoengine.wtf import model_form

from model import esporte_dao
from model import Esporte

EsporteForm = model_form(Esporte)


# class EsporteForm(FlaskForm):
#     # id_esporte = IntegerField('Id Esporte', validators=[DataRequired()],
#     #                           render_kw={'value': f'{esporte_dao.select_next_id()}',
#     #                                      'disabled': '', 'readonly': ''})
#     nome = StringField('Nome', validators=[DataRequired()])
