import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def conversor():
    valor_convertido = ''
    if request.method == 'POST' and 'valor_a_converter' in request.form:
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao = requisicao.json()
        cotacao = float(cotacao['USD']['bid'])
        cotacao = round(cotacao, 2)
        valor = request.form.get('valor_a_converter')
        valor = float(valor)
        valor = round(valor, 2)
        valor_convertido = round((cotacao * valor),2)
    return render_template('index.html', valor_a_converter=valor_convertido)

app.run()
