from flask import Blueprint, render_template

ws = Blueprint(
    'main',
    __name__,
    template_folder = "templates"
)

@ws.route("/ws/")
def index():
    return render_template("ws/index.html")
