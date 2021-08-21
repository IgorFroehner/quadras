from flask import Blueprint, render_template, redirect

from model import evento_dao as dao
from forms import EventoForm

blue = Blueprint('evento', __name__, static_folder='static', template_folder='templates')


@blue.route('/evento')
def evento():
    rows = dao.select_all()
    table = []
    for row in rows:
        table.append({
            'Título': row.titulo,
            'Início:': row.inicio,
            'Fim': row.fim,
            'Blocos': ''.join([f'{bloco}, ' for bloco in row.blocos])
        })
    return render_template('table.html', title='Evento', table=table)


@blue.route('/evento_form', methods=['GET', 'POST'])
def evento_form():
    form = EventoForm()
    erro = None
    if form.validate_on_submit():
        dao.insert_from_dict(form.data)
        return redirect('/evento')
    return render_template('form.html', title='Evento', form=form, erro=erro)
