from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, redirect

from model import evento_dao as dao
from forms import EventoForm

blue = Blueprint('evento', __name__, static_folder='static', template_folder='templates')


@blue.route('/evento')
def evento():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Evento', table=table)


@blue.route('/evento_form', methods=['GET', 'POST'])
def evento_form():
    form = EventoForm()
    erro = None
    if form.validate_on_submit():
        try:
            dao.insert_from_dict(form.data)
        except SQLAlchemyError as e:
            erro = e
            return render_template('form.html', title='Agendamento', form=form, erro=erro)
        return redirect('/evento')
    return render_template('form.html', title='Evento', form=form, erro=erro)
