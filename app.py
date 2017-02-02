from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/api')
def api_index():
    str = dict(name='Hetal',city='Columbus',state='OH')
    return jsonify(str)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug = True, port=5000)
