from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/classify", methods=["POST"])
def classify():
    data = request.json
    # Process input data and perform classification
    result = {"prediction": "Class A", "confidence": 0.95}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)