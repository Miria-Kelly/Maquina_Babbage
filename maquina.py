import leitor, moinho, armazen, impressora

arquivo_entrada = "cartao.in"
arquivo_saida = "cartao.out"

def configurar(nome_arquivo_entrada = 'cartao.in', nome_arquivo_saida = 'cartao.out'):
    global arquivo_entrada, arquivo_saida
    arquivo_entrada = nome_arquivo_entrada
    arquivo_saida = nome_arquivo_saida
    #print(f'ok.{arquivo_entrada}')
    #print(f'ok. {arquivo_saida}')


def ligar_maquina():
    codigo, posicao, numeros = leitor.ler_cartao(arquivo_entrada)
    resultado = []
    limpar_arquivo = True

    for c in range(0, len(codigo)):
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
            impressora.escrever(valor, arquivo_saida, limpar_arquivo)
            limpar_arquivo = False  


configurar("cartao.in", "cartao.out")
ligar_maquina()