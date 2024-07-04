from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST, GET"])
def hook():
    print("Helllo")
    return "demo helllo"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")