# definir função
def jogar():
    print('********************************')
    print('Bem vindo ao jogo da forca')
    print('********************************')

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    print(letras_acertadas)
    #enquanto (true) and (true)
    while(not enforcou and not acertou):
        chute = input("Qual é a letra? ")
        # devolve uma string sem espaços
        chute = chute.strip()

        #posição
        index = 0          
        # para cada letra dentro da minha palavra secreta, exibe letra por letra
        for letra in palavra_secreta:
            #count é o número de ocorrências de algum item
            letras_faltando = str(letras_acertadas.count('_'))

            #comparando somente as letras maiuscula
            if (chute.upper() == letra.upper()):
                #print('Encontrei a letra "{}" na posição "{}"'.format(letra, index))
                #letras_acertadas pega o index e recebe o input da letra, então substitui a letra acertada no array letras_acertadas
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
        print("Jogando...")

if (__name__ == "__main__"):
    jogar()
