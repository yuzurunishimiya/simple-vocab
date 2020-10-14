from flask import Blueprint, render_template, jsonify
from helper import dbs

db_adj = dbs["adjectives"]

adjective_bp = Blueprint("adjective", __name__)

@adjective_bp.route("/adjective")
def adjective_view():
    data = list(db_adj.aggregate([
        {"$sort": {"english": 1}},
        {"$project": {
            "_id": 0,
            "example": 0,
            "explanation": 0
        }}
    ]))
    return render_template("adjective.html", data=data)

@adjective_bp.route("/adjective/detail/<english>")
def get_detail(english):
    data = db_adj.find_one({"english": english}, {"_id": 0})
    return jsonify(data)
