from flask import Blueprint, render_template

from helper import dbs

noun_bp = Blueprint("noun", __name__)

@noun_bp.route("/noun")
def noun_view():
    data = dbs.nouns.find({}, {"_id": 0}).sort([("english", 1)])
    temp = {}
    for i in data:
        if i["english"][0] not in temp:
            temp[i["english"][0]] = [i]
        else:
            temp[i["english"][0]].append(i)
    print(temp)

    return render_template("noun.html", data=temp)

