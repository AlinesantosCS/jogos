import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    # round - arrendonda | random.random chama na a função | 0 até 100
    # ranrange mostra de 1 a 100
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    #rodada = 1

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #while (rodada <= total_de_tentativas):

    # rodada(váriavel) - range(começa com 1 e vai até total tentativas, no entranto não mostra o último número por isso o +1
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            #Não sai do laço e continua para a próxima interação
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior que o número secreto")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

                pontos_perdidos = abs(numero_secreto - chute) # 40 - 20
                pontos = pontos - pontos_perdidos
                rodada = rodada + 1

    print("Fim do jogo")

#   name - nome do jogo será setado como main, ou quando for executado diretamente, assim não vai executar dois jogos de uma vez por conta da função
if(__name__ == "__main__"):
    jogar()

    # # Casas decimais
    # print("R$ {:.2f}".format(1.5))
    # # Quantidade caracteres no total, pode colocar 0 a esquerda
    # print("R$ {:09.2f}".format(1852.698))
    # d -> números inteiros
    # print("R$ {:06d}".format(1852))



