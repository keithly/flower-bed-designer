from flask import Flask
from werkzeug.utils import find_modules, import_string
from config import Config
from flower_bed_designer import helpers
from flower_bed_designer.blueprints.plant import views


def register_blueprints(app):
    for name in find_modules('flower_bed_designer.blueprints', recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


def create_app(test_config=None):
    app = helpers.ApiFlask(__name__)

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    app.register_error_handler(helpers.ApiException, lambda err: err.to_result())
    register_blueprints(app)

    return app
