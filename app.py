from flask import Flask
from flask import abort, request, jsonify, render_template

from routes import adjective_bp
from routes import adverb_bp
from routes import noun_bp
from routes import verb_bp

app = Flask(__name__)
app.register_blueprint(adjective_bp)
app.register_blueprint(adverb_bp)
app.register_blueprint(noun_bp)
app.register_blueprint(verb_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)