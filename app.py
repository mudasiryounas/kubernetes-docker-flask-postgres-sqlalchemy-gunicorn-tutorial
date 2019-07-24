from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import User

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy()
db.init_app(app)


@app.route('/test')
def test():
    return 'Hello World! I am from docker!'


@app.route('/db_test')
def test_db():
    db.create_all()
    db.session.commit()

    u = User(name='Mudasir', surname='Younas')
    db.session.add(u)
    db.session.commit()

    user = User.query.first()
    return "User '{} {}' is from database".format(user.name, user.surname)
