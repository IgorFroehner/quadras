from flask import Blueprint, render_template, redirect

from model import quadra_dao as dao
from forms import QuadraForm

blue = Blueprint('quadra', __name__, static_folder='static', template_folder='templates')


@blue.route('/quadra')
def quadra():
    rows = dao.select_all()
    table = []
    for row in rows:
        table.append({
            'Largura': row.largura,
            'Comprimento': row.comprimento,
            'Bloco': row.bloco.id_bloco,
            'Espores': ''.join([f'{esporte}, ' for esporte in row.esportes])
        })
    return render_template('table.html', title='Quadra', table=table)


@blue.route('/quadra_form', methods=['GET', 'POST'])
def quadra_form():
    form = QuadraForm()
    print(form.data)
    if form.validate_on_submit():
        dao.insert_from_dict(form.data)
        return redirect('/quadra')
    return render_template('form.html', title='Quadra', form=form)
