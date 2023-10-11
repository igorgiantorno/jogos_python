import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = escolhe_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0

    usuario = str(input ("Como posso te chamar? "))
    print("\nOlá", usuario, ", para não se enforcar, tente adivinhar a palavra, você tem 6 tentativas...\n")
    print(letras_acertadas)
    
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            
        else:
            erros += 1
            print("\nEsta letra não existe, Tentativa {} de {}\n".format(erros, "8"))
            desenha_forca(erros)

        enforcou = erros == 8
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor(usuario, palavra_secreta)
    else:
        imprime_mensagem_perdedor(usuario, palavra_secreta)
        
    print("Fim de jogo!\n")

def imprime_mensagem_abertura():
    print("------Tente adivinhar a palavra-------")
    print("--Você tem 6 possibilidades de erro---")
    print("----------NÃO SE ENFORQUE!!-----------\n")

def escolhe_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close() 

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("\nQual Letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas [index] = letra
        index += 1

def imprime_mensagem_vencedor(usuario, palavra_secreta):
        print("\nParabéns {}, você acertou a palavra que é {} e GANHOU O JOGO!!\n".format(usuario, palavra_secreta))
        print("uoooolll , YOU WIN!")
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

def imprime_mensagem_perdedor(usuario, palavra_secreta):
        print("\nVocê esgotou suas tentativas {} e se perdeu. A palavra era {} :/\n".format(usuario, palavra_secreta))
        print("Puxa, você foi enforcado!")
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

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
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

if(__name__ == "__main__"):
    jogar()