
from flask import Flask, render_template
from decouple import config
from flask_mongoengine import MongoEngine

app = Flask(__name__)


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


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
