from flask import Flask
from .model import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.cfg', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    """init db here"""
    db.init_app(app)

    """register blueprint"""
    from .controller import user
    app.register_blueprint(user.bp)

    return app
