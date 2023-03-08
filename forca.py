import random
def jogar():

    print("**********************************")
    print("***Bem vindo ao jogo de Forca!!***")
    print("**********************************")

    arquivo = open("palavras.txt", "r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))

    palavra_secreta = palavra[numero].upper()
    letras_acertadas = ["_" for letras in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print ("Você ganhou!")
    else:
        print ("Você perdeu!")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()