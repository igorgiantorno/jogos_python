import forca
import adivinhacao

print("--------------------------------------")
print("-----------Olá, Bem-vindo-------------")
print("--------Escolha o seu jogo!-----------")
print("--------------------------------------\n")

print("----(1) Forca   (2) Adivinhação-------\n")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("\nVocê escolheu FORCA, Boa sorte.\n")
    forca.jogar()
elif(jogo == 2):
    print("\nVocê escolheu ADIVINHAÇÃO, Boa sorte.\n")
    adivinhacao.jogar()


            #print("Fim de jogo!")