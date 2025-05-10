from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message= "olá, mundo!"), 200

@app.route('/senai', methods=['GET'])
def senai():
    return jsonify(message= "olá, turma de Python com Framework!"), 200

#endpoint pesquisa endereço através do cep, retorna em formato json
@app.route('/pesquisacep/<cep>', methods=['GET'])
def pesquisacep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    return resposta.json()

if __name__ == '__main__':
    app.run(debug=True)