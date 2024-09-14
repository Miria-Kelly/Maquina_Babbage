def escrever(valor, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'a') as cartao:
        memoria_out = [0] * 16
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

