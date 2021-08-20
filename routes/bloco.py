from flask import Blueprint, render_template, redirect

from model import bloco_dao as dao
from forms import BlocoForm

blue = Blueprint('bloco', __name__, static_folder='static', template_folder='templates')


@blue.route('/bloco')
def bloco():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Bloco', table=table)


@blue.route('/bloco_form', methods=['GET', 'POST'])
def bloco_form():
    form = BlocoForm()
    if form.validate_on_submit():
        dao.insert_from_dict(form.data)
        return redirect('/bloco')
    return render_template('form.html', title='Bloco', form=form)
