from datetime import datetime

def printf(msg,tam=40):
    print(f'{msg:^{tam}}')


def linha(tam=40):
    print('\033[0;94m~\033[0;93m' * tam)


def colorido(cor='branco'):
    print('\033',end='')


def criarq(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        try:
            a = open(arq, 'wt+')
            a.close()
        except:
            print('\033[1;31mERRO AO CRIAR ARQUIVO\033[m')
        else:
            print('\033[0;32mARQUIVO CRIADO COM SUCESSO\033[m')
    else:
        print('\033[0;32mARQUIVO ACESSADO COM SUCESSO\033[m')


def escrevearq(arq, jogo):
    a = open(arq , 'at')
    data = datetime.now().date()
    a.write(f'{jogo}:{data}\n')


def conferedata(arq, data=datetime.now().date()):
    jogos = []
    jafoi = []
    try:
        a = open(arq, 'rt')
    except:
        print('\033[1;31mERRO AO LER ARQUIVO\033[m')
    else:
        for c in a:
            b = c.replace('\n', '').split(':')
            if b[1] == data:
                jogos.append(b[0])
            else:
                jafoi.append(b[0])


def numerosorteio():
    from urllib import request

    a = request.urlopen('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')
'''    print('erro')
    print(a.read())'''

numerosorteio()
