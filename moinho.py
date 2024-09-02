import armazen
valores_carregados = []


def carregar(posicao):
    num = armazen.carregar(posicao)
    valores_carregados.append(num)

    return valores_carregados

def somar():
    resultado = valores_carregados[0] + valores_carregados[1]
    return resultado

def subtrair ():
    resultado = (valores_carregados[0] - valores_carregados[1])
    return resultado

def multiplicar():
    resultado = valores_carregados[0] * valores_carregados[1]
    return resultado

def armazenar_resultado(resultado, posicao):
    return armazen.armazenar(resultado, posicao)














"""def LOADOP(valor, posicao):
    #carrega valor na posicao da memoria fornecida

def ADD(a, b):
    #soma dois operadnos que foram carregados no moinho

def SUB(a, b):
    #subtrai os dois valores que foram carregados no moinho

def MUL(a, b):
    #multiplica  os dois valores que forams careegados no moinho

def STORE(resultado):
    #armazena o resultado ultima operaçao realizada no moinho

def PRINT(valor):
    #escreve o conteudo da posicao dada do armazem"""