from flask import Flask, request
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/unifor-ead', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!';

@app.route('/unifor-nome', methods=['GET'])
def info_nome():
    nome = request.args.get('nome');
    return nome;


if __name__ == '__main__':
    app.run()
