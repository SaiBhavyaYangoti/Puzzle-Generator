from flask import Flask, render_template, request, jsonify
from puzzles.english_puzzles import get_english_puzzles
from puzzles.math_puzzles import get_math_puzzles
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/english")
def english():
    return render_template("english.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/get_puzzles")
def get_puzzles():
    puzzle_type = request.args.get("type")
    category = request.args.get("category")  # This line is critical

    if category == "english":
        puzzles = get_english_puzzles(puzzle_type)
    elif category == "math":
        puzzles = get_math_puzzles(puzzle_type)
    else:
        puzzles = []

    return jsonify(puzzles)


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)  # or add host/port if needed
