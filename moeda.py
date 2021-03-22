class Moeda():
    def __init__(self, moedas1):
        self.moedas = moedas1

    def pega_moeda(self):
        dinheiro = self
        moeda1 = ''

        if dinheiro == 'Peso Argentino':
            moeda1 = 'ARS'
        elif dinheiro == 'Dólar Australiano':
            moeda1 = 'AUD'

        elif dinheiro == 'Bitcoin':
            moeda1 = 'BTC'

        elif dinheiro == 'Dólar Canadense':
            moeda1 = 'CAD'

        elif dinheiro == 'Franco Suíço':
            moeda1 = 'CHF'

        elif dinheiro == 'Remimbi':
            moeda1 = 'CNY'

        elif dinheiro == 'Ethereum':
            moeda1 = 'ETH'

        elif dinheiro == 'Euro':
            moeda1 = 'EUR'

        elif dinheiro == 'Novo Shekel Israelense':
            moeda1 = 'ILS'

        elif dinheiro == 'Dólar Americano':
            moeda1 = 'USD'

        elif dinheiro == 'Tether':
            moeda1 = 'USDT'

        elif dinheiro == 'Libra Esterlina':
            moeda1 = 'GBP'

        elif dinheiro == 'Litecoin':
            moeda1 = 'LTC'

        elif dinheiro == 'Iene Japonês':
            moeda1 = 'JPY'


        elif dinheiro == 'Ripple':
            moeda1 = 'XRP'

        dindin = moeda1 + '-BRL'

        return moeda1, dindin


if __name__ == '__main__':
    moedas = 'Remimbi'
    dados_moeda = Moeda.pega_moeda(moedas)
    cod_moeda = dados_moeda[0]
    convert_moeda = dados_moeda[1]
    print(cod_moeda)
    print(convert_moeda)

    '''
    requisicao = requests.get(f'https://economia.awesomeapi.com.br/all/{cod_moeda}')
    cotacao = requisicao.json()
    cotacao = float(cotacao[cod_conversor]['bid'])
    cotacao = round(cotacao, 2)
    valor = request.form.get('valor_a_converter')
    valor = float(valor)
    valor = round(valor, 2)
    valor_convertido = round((cotacao * valor), 2)
'''


