from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from .views import view

        app.register_blueprint(view, url_prefix="/")

        return app
