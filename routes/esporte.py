from flask import Blueprint, render_template, redirect

from model import esporte_dao as dao
from forms import EsporteForm

blue = Blueprint('esporte', __name__, static_folder='static', template_folder='templates')


@blue.route('/esporte')
def esporte():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Esporte', table=table)


@blue.route('/esporte_form', methods=['GET', 'POST'])
def esporte_form():
    form = EsporteForm()
    if form.validate_on_submit():
        dao.insert_from_dict(form.data)
        return redirect('/esporte')
    return render_template('form.html', title='Esporte', form=form)
