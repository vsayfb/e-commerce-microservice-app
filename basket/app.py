import flask
from flask import request, jsonify
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello Flask'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=83)
