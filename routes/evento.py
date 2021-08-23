from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

from model import evento_dao as dao
from model import usuario_dao
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
            'Blocos': ', '.join([f'{bloco}' for bloco in row.blocos])
        })
    return render_template('table.html', title='Evento', table=table)


@blue.route('/evento_form', methods=['GET', 'POST'])
@login_required
def evento_form():

    user = usuario_dao.find_by_email(current_user.email)
    print(user.permissao)
    if user and user.permissao == 'adm':
        form = EventoForm()
        erro = None
        if form.validate_on_submit():
            dao.insert_from_dict(form.data)
            return redirect('/evento')
        return render_template('form.html', title='Evento', form=form, erro=erro)
    else:
        from app import unauthorized

        return unauthorized()
