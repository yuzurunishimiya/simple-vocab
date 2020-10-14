from flask import Blueprint, render_template
from helper import dbs

adverb_bp = Blueprint("adverb", __name__)

@adverb_bp.route("/adverb")
def adverb_view():
    return render_template("adverb.html")

