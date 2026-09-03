from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
   marks= {
    "Rohan": 90,
    "Sohan": 80,
    "Mohan": 70,
    "Sumit": 60,
}
   values = [1, marks, 67]
   return jsonify(values)

app.run(debug=True)
