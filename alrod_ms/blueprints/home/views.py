from flask import Blueprint, render_template
import helpers.env as env

home = Blueprint(
    'home',
    __name__,
    template_folder = 'templates'
)

@home.route("/")
def index():
    return render_template("home/index.html", app_name = env.APP_NAME)
