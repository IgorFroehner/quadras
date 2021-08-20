from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, redirect

from model import agendamento_dao as dao
from forms import AgendamentoForm


blue = Blueprint('agendamento', __name__, static_folder='static', template_folder='templates')


@blue.route('/agendamento')
def agendamento():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Agendamento', table=table)


@blue.route('/agendamento_form', methods=['GET', 'POST'])
def agendamento_form():
    form = AgendamentoForm()
    erro = None
    if form.validate_on_submit():
        try:
            dao.insert_from_dict(form.data)
        except SQLAlchemyError as e:
            erro = e
            return render_template('form.html', title='Agendamento', form=form, erro=erro)
        return redirect('/agendamento')
    return render_template('form.html', title='Agendamento', form=form, erro=erro)
