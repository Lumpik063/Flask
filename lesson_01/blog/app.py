from flask import Flask, render_template

from blog.report.views import report
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprints(user)
    app.register_blueprints(report)


@user.route('/')
def index():
    return render_template('index.html')
