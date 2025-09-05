from flask import Flask
from .db import db
from .routes import bp as routes_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@db:5432/bookwish",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    app.register_blueprint(routes_bp)

    @app.route("/healthz")
    def healthz():
        return {"status": "ok"}

    return app
