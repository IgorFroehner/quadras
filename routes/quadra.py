from flask import Blueprint, render_template, redirect, jsonify
from flask_login import login_required

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
            'Espores': ', '.join([f'{esporte}' for esporte in row.esportes])
        })
    return render_template('table.html', title='Quadra', table=table)


@blue.route('/quadra/esporte/<id_quadra>')
def esportes_quadra(id_quadra: str):
    esportes = dao.find_esportes(id_quadra)
    if len(esportes) >= 1:
        print(esportes)
        return jsonify(esportes), 200
    else:
        return None, 404


@blue.route('/quadra_form', methods=['GET', 'POST'])
@login_required
def quadra_form():
    form = QuadraForm()
    if form.validate_on_submit():
        dao.insert_from_dict(form.data)
        return redirect('/quadra')
    return render_template('form.html', title='Quadra', form=form)
