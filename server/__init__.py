from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'


    from .code import code
    from .decode import decode
    from .choice import choice
    from .showdb import db


    app.register_blueprint(code, url_prefix='/')
    app.register_blueprint(decode, url_prefix='/')
    app.register_blueprint(choice, url_prefix='/')
    app.register_blueprint(db, url_prefix='/')
    return app