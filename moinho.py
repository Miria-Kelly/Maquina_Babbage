import armazen
valores_carregados = []

resultado = 0

def carregar(posicao):
    global valores_carregados
    num = armazen.carregar(posicao)
    valores_carregados.append(num)

def somar():
    global resultado
    resultado = valores_carregados[0] + valores_carregados[1]
    return resultado

def subtrair ():
    global resultado
    resultado = (valores_carregados[0] - valores_carregados[1])
    return resultado

def multiplicar():
    global resultado
    resultado = valores_carregados[0] * valores_carregados[1]
    return resultado

def armazenar_resultado(posicao):
    global resultado
    armazen.armazenar(resultado, posicao)
