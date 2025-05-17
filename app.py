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

@app.route('/climapp/sp', methods=['GET'])
def climapp(sp):
    cidade = "presidente prudente"
    key = "6a22d2d0dda77e80ca0d1492b2f06554"
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q{cidade}&lang=pt"
    resposta = requests.get(url)
    return resposta.json()    

if __name__ == '__main__':
    app.run(debug=True)