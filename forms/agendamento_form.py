from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired

from model import quadra_dao, esporte_dao


class AgendamentoForm(FlaskForm):
    date = DateField("Data Agendamento", validators=[DataRequired()])
    hora = TimeField("Hora Agendamento", validators=[DataRequired()])
    quadra = SelectField("Quadra", validators=[DataRequired()], coerce=int)
    esporte = SelectField("Esporte", validators=[DataRequired()], coerce=int)

    def __init__(self):
        super(AgendamentoForm, self).__init__()
        self.quadra.choices = [(quadra.id_quadra,
                                f'(Bloco: {quadra.id_bloco}; Quadra: {quadra.id_quadra}): {quadra.largura}m X'
                                f' {quadra.comprimento}m') for quadra in quadra_dao.select_all()]
        self.esporte.choices = [(esporte.id_esporte, esporte.nome) for esporte in esporte_dao.select_all()]
