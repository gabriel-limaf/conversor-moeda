"""
Conversor de moeda em Python by Gabriel Lima

Euro = EUR
Dolar = USD
Libra = GBP

"""

import requests
print('Bem-vindo ao conversor de moedas em Python!')


def inicio():

    moeda = int(input('Qual moeda deseja converter?\n'
                      'Dólar: Digite 1\n'
                      'Euro: Digite 2\n'
                      'Libra: Digite 3\n'
                      'Encerrar Programa: Digite 4\n'))
    if moeda < 1 or moeda > 4:
        print("Escolha um valor válido \n")
        inicio()
    if moeda == 1:
        usd_real()
    if moeda == 2:
        eur_real()
    if moeda == 3:
        libra_real()
    if moeda == 4:
        exit()


# Real para Dólar
def usd_real():
    requisicao_dolar = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao_dolar = requisicao_dolar.json()
    print('#### Cotação do Dolar ####')
    # print('Moeda: ' + cotacao_dolar['USD']['name'])
    print('Data: ' + cotacao_dolar['USD']['create_date'])
    print('Valor atual: R$' + cotacao_dolar['USD']['bid'])
    val_dolar = float(cotacao_dolar['USD']['bid'])
    val_real = float(input('Qual o valor em Real deseja converter para Dólar?: '))
    print(f'{val_real} Reais é {val_real/val_dolar} Dólares \n')
    inicio()


# Real para Euro
def eur_real():
    requisicao_euro = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
    cotacao_euro = requisicao_euro.json()
    print('#### Cotação do Euro ####')
    # print('Moeda: ' + cotacao_euro['EUR']['name'])
    print('Data: ' + cotacao_euro['EUR']['create_date'])
    print('Valor atual: R$' + cotacao_euro['EUR']['bid'])
    val_euro = float(cotacao_euro['EUR']['bid'])
    val_real = float(input('Qual o valor em Real deseja converter para Euro?: '))
    print(f' {val_real} Reais é {val_real / val_euro} Euros \n')
    inicio()


# Real para Libras Esterlinas
def libra_real():
    requisicao_libra = requests.get('https://economia.awesomeapi.com.br/all/GBP-BRL')
    cotacao_libra = requisicao_libra.json()
    print('#### Cotação da Libras Esterlinas ####')
    # print('Moeda: ' + cotacao_libra['GBP']['name'])
    print('Data: ' + cotacao_libra['GBP']['create_date'])
    print('Valor atual: R$' + cotacao_libra['GBP']['bid'])
    val_libra = float(cotacao_libra['GBP']['bid'])
    val_real = float(input('Qual o valor em Real deseja converter para Libras?: '))
    print(f' {val_real} Reais é {val_real / val_libra} Libras Esterlinas \n')
    inicio()


inicio()
