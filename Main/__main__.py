from flask import Flask
from utilities import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Website working!"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=13337)