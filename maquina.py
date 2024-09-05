import leitor, moinho, armazen, impressora

resultado = []

codigo, posicao, numeros = (leitor.ler_cartao("cartao.in"))

for c in range(0,len(codigo)):
    if codigo[c] == "0001":
        memoria = armazen.armazenar(numeros[c], posicao[c])

    elif codigo[c] == "0010":
        moinho.carregar(posicao[c])

    elif codigo[c] == "0011":
        soma = moinho.somar()
        resultado.append(soma)
    elif codigo[c] == '0100':
        subtracao = moinho.subtrair()
        resultado.append(subtracao)
    elif codigo[c] == "0101":
        multi = moinho.multiplicar()
        resultado.append(multi)

    elif codigo[c] == "0110":
        moinho.armazenar_resultado(posicao[c])

    elif codigo[c] == "0111":
        valor = armazen.carregar(posicao[c])
        valor = bin(valor)[2:]
        valor = str(valor)

        impressora.escrever(valor)

impressora.cartao.close()


