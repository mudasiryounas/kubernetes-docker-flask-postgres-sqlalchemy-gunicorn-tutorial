from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.cfg', silent=False)

db = SQLAlchemy()
db.init_app(app)


@app.route('/')
def test():
    return 'Hello World!'

@app.route('/db_test')
def test():

    return 'Hello World!'