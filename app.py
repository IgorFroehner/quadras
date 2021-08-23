import flask
from flask import Flask, render_template, redirect
from decouple import config
from flask_mongoengine import MongoEngine
import flask_login
from flask_login import login_user, logout_user, login_required

app = Flask(__name__)
login_manager = flask_login.LoginManager()


def config_app(_app):
    db_pass = config('MONGO_PASS')
    db_user = config('MONGO_USER')
    _app.config['SECRET_KEY'] = config('SECRET_KEY')
    _app.config['MONGODB_SETTINGS'] = {
        'host': f'mongodb+srv://{db_user}:{db_pass}@cluster0.ogn2b.mongodb.net/quadras?retryWrites=true&w=majority'
    }
    _db = MongoEngine(app)
    return _app, _db


def register_routes(_app):
    from routes import blueprints
    for blueprint in blueprints:
        _app.register_blueprint(blueprint)
    return _app


app, db = config_app(app)
app = register_routes(app)
login_manager.init_app(app)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@login_manager.user_loader
def user_loader(email):
    from model import Usuario
    return Usuario.objects.get(email=email)


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html', erro=True)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    from forms import LoginForm
    from model import usuario_dao

    form = LoginForm()
    if form.validate_on_submit():
        user = usuario_dao.find_by_email(form.email.data)
        if user is not None:
            if user.senha == form.senha.data:
                flask.flash('Logged in Successfully.')
                login_user(user)
                return redirect('/')
        else:
            return render_template('login.html', form=form, erro='Email ou senha incorretos')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
