from flask import Blueprint, render_template
from helper import dbs


verb_bp = Blueprint("verb", __name__)

@verb_bp.route("/verb")
def verb_view():

    return render_template("verb.html")

