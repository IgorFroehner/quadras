from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired

from model import quadra_dao, esporte_dao


class AgendamentoForm(FlaskForm):
    date = DateField("Data Agendamento", validators=[DataRequired()])
    hora = TimeField("Hora Agendamento", validators=[DataRequired()])
    quadra = SelectField("Quadra", validators=[DataRequired()])
    esporte = SelectField("Esporte", validators=[DataRequired()])

    def __init__(self):
        super(AgendamentoForm, self).__init__()
        self.quadra.choices = [(quadra,
                                f'(Bloco: {quadra.bloco.id_bloco}; Quadra: {quadra.largura}m X'
                                f' {quadra.comprimento}m)') for quadra in quadra_dao.select_all()]
        self.esporte.choices = [(esporte.nome, esporte.nome) for esporte in esporte_dao.select_all()]
