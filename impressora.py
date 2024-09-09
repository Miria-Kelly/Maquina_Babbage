cartao = open('cartao.out', 'w')
def escrever(valor):
    while len(valor) <8:
        valor = "O" + valor
    cartao.write("OOOO OOOO ")
    
    for c in valor:
        if c == '1':
            valor = valor.replace("1", "X")

        else:
            valor = valor.replace('0', 'O')
    tam = len(valor)
    cont = 0

    for c in valor:
        cont += 1
        cartao.write(c)
        if cont % 4 == 0 and cont != tam:
            cartao.write(' ')
    cartao.write('\n')

