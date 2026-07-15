from ai_agent import learn_code, review_code, fix_code
from db import save_review
from db import get_stats
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from runner import run_python_code
from db import save_code

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("AICRA_v2.html")

@app.route("/game_runner")
def game_runner():
    return render_template("python_game.html")

@app.route("/run", methods=["POST"])
def run():

    code = request.json["code"]

    print("Received:", code)

    save_code(code)

    output = run_python_code(code)

    return jsonify({"output": output})

from db import save_review


@app.route("/fix", methods=["POST"])
def fix():

    code = request.json["code"]

    fixed, reason = fix_code(code)

    return jsonify({
        "fixed_code": fixed,
        "reason": reason
    })


@app.route("/learn", methods=["POST"])
def learn():

    code = request.json["code"]

    lesson = learn_code(code)

    return jsonify({
        "lesson": lesson
    })


@app.route("/review", methods=["POST"])
def review():

    code = request.json["code"]

    return jsonify({
        "message": "Code looks OK"
    })

@app.route("/save", methods=["POST"])
def save():

    code = request.json["code"]

    save_code(code)

    return {"status": "saved"}

@app.route("/stats")
def stats():

    data = get_stats()

    return data

if __name__ == "__main__":
    app.run(debug=True)
    