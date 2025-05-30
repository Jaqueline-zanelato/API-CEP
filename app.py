from flask import Flask, jsonify,render_template, requests
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

@app.route('/tempo', methods=['GET','POST'])
def tempo():
    cidade = request.args.get("cidade")
    key = "c4380707dde242f4b78202712252204"
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={cidade}&lang=pt"
    resposta = requests.get(url)
    result = resposta.json()

    temperatura = result["current"]["temp_c"]
    umidade = result["current"]["humidity"]
    local_tempo = result["location"]["localtime"]
    regiao = result["location"]["region"]
    velocidade_vento = result["current"]["vis_km"]
    pressao = result["current"]["pressure_mb"]

    return render_template("monitoramento.html",temp=temperatura, umid=umidade, localtime=local_tempo, region=regiao, vis_km=velocidade_vento, pressure_mb=pressao, cidade=cidade)  

if __name__ == '__main__':
    app.run(debug=True)