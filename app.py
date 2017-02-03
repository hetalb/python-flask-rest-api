from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/api')
def api_index():
    str = dict(name='John Doe',city='New York',state='NY')
    return jsonify(str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=5000)
