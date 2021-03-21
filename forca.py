import random


# definir função
def jogar():
    imprime_mensagem_abertura()

    # executa a função e devolve o retorno da função
    palavra_secreta = carrega_palavra_secreta()

    # Outra forma chamada Compreensão de lista
    letras_acertadas = ["_" for letra in palavra_secreta]
    # Torna palavra mais dinâmica pois, de acordo com o tamanho da palavra secreta vai adicionar "_"
    # for letra in palavra_secreta:
    #   letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros: int = 0
    print(letras_acertadas)

    # enquanto (true) and (true)
    while not enforcou and not acertou:

        chute = pede_chute()

        # Se o chute tiver dentro da palavra_secreta
        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros + 1
            desenha_forca(erros)

        # Variável enforcou receber 6 torna-se true e vai para o fim de jogo
        enforcou = erros == 7

        # Se não tiver "_" na letrar_acertadas significa que o usuário acertos a palavra
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        print(f'Faltam {6 - erros} tentativas ')

        # print('Ainda faltam acertar {} letras'.format(letras_faltando))
        print("Jogando...")

    if acertou:
        imprime_mensagem_vencedor()

    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print("*********************************")
    print("   Bem vindo ao jogo da Forca!   ")
    print("*********************************")


def carrega_palavra_secreta():
    # Abre e modifica um arquivo
    # (nome do arquivo, tipo de modificador(r,w,a,b))
    """
    read(r) -  Leitura
    write(w) - Escrita
    append(a) - Adicionar
    binary(b) - Binário(imagens)
    """
    arquivo = open("palavras.txt", "r")
    palavras = []
    # acessando cada linha dentro do arquivo
    for linha in arquivo:
        # strip tira o \n de cada linha
        linha = linha.strip()
        palavras.append(linha)

    # Depois de modificar o arquivo, sempre fechar
    # arquivo.close()

    '''
    Com a maneira acima o arquivo não será fechado quando ocorrer
    algum erro, já o abaixo o Python se encarregá de fechar.
    '''
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            print(linha)

    # do 0 até o comprimento quantidade de elementos da lista palavras
    numero = random.randrange(0, len(palavras))

    # palavra_secreta = "maça".upper()
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def pede_chute():
    chute = input("Qual é a letra? ")
    # strip - devolve uma string sem espaços e sem \n
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    # posição
    index = 0
    '''for - in :
    verificar se um determinado elemento existe em uma Lista, 
    podemos utilizar o operador in. Ele nos retorna 
    True ou False caso o elemento esteja ou não dentro 
    da lista verificada'''
    # para cada letra dentro da minha palavra secreta, exibe letra por letra
    for letra in palavra_secreta:
        # count é o número de ocorrências de algum item
        letras_faltando = str(letras_acertadas.count('_'))

        # comparando somente as letras maiuscula
        if chute == letra:
            # print('Encontrei a letra "{}" na posição "{}"'.format(letra, index))

            letras_acertadas[index] = letra
        index = index + 1


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
