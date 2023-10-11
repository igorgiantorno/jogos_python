import random

def jogar():

    print("---------------Tente adivinhar o numero secreto--------------")
    print("----Sua pontuação é baseada nos numeros que você escolhe-----")
    print("-------------Escolha sua dificuldade e desafie-se------------\n")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    usuario = str(input ("Qual seu nome? "))

    print("\nOlá", usuario, ", Qual nivel de dificuldade você gostaria de tentar?\n")
    print("(1) Fácil  (2) Médio (3) Difícil")

    nivel = int(input("\nEscolha um nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
        print("\nVocê terá 20 tentativas, moleza. Vamos lá!")
    elif(nivel == 2):
        total_de_tentativas = 10
        print("\nVocê terá 10 tentativas, me mostre do que é capaz! Vamos lá!")
    else:
        total_de_tentativas = 5
        print("\nVocê terá 5 tentativas, eu duvido... Vamos lá!")

    print("\nBoa sorte, ", usuario)

    for rodada in range (1, total_de_tentativas + 1):
        print("\nTentativa {} de {}\n".format(rodada, total_de_tentativas))

        chute_str = input("Digite um numéro entre 1 e 100: ")
        print("\nVocê digitou:", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!!")
            continue

        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("\nUal, {}, parabéns, você acertou e fez: {} pontos!!\n".format(usuario, pontos))
            break
        else:
            if (chute_maior):
                print("\nUuuhhhh, que pena, Voce errou! Tente um numero mais baixo", usuario,".\n")
            elif (chute_menor):
                print("\nUuuhhhh, que pena, Voce errou! Tente um numero mais alto", usuario,".\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("\nEste é o numero secreto:", numero_secreto)

    print("\nFim de jogo!")

if(__name__ == "__main__"):
    jogar()