from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

from model import bloco_dao, esporte_dao


class QuadraForm(FlaskForm):
    largura = FloatField('Largura', validators=[DataRequired()])
    comprimento = FloatField('Comprimento', validators=[DataRequired()])
    bloco = SelectField('Bloco',
                        choices=[(bloco.id_bloco, bloco.id_bloco) for bloco in bloco_dao.select_all()],
                        validators=[DataRequired()])
    esportes = SelectMultipleField('Esportes',
                                   choices=[(esporte.nome, esporte.nome) for esporte in esporte_dao.select_all()])

    def __init__(self):
        super(QuadraForm, self).__init__()
        self.bloco.choices = [(bloco.id_bloco, bloco.id_bloco) for bloco in bloco_dao.select_all()]
        self.esportes.choices = [(esporte.nome, esporte.nome) for esporte in esporte_dao.select_all()]
