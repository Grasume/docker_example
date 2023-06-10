from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route("/get_ip", methods=["GET"])
def get_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)