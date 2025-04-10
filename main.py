from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API CHK ATIVA"

@app.route('/chk', methods=['POST'])
def chk():
    data = request.json
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)