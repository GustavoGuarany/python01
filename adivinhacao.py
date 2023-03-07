def jogar():

    import random

    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    numero_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade?")

    nivel = int( input (" (1) Fácil (2) Médio (3) Difícil :"))

    if (nivel == 1):
        numero_tentativas = 20
    elif (nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5


    for rodada in range(1 , numero_tentativas + 1 ):
        print("Numero de tentativas: {} de {}".format(rodada, numero_tentativas))
        chute_str = input("Digite um número de 1 a 100:")
        print ("Você digitou o numero: ", chute_str)
        chute = int(chute_str)



        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero de 1 a 100")
            continue

        if (acertou):
            print ("Você acertou e sua pontuação foi {}" .format(pontos))
            break
        else:
            if(maior):
                print("Você chutou um numero maior!")
            elif(menor):
                print ("Você chutou um numero menor!")
            pontos_perdidos = abs((numero_secreto - chute))
            pontos = pontos - pontos_perdidos
            print(pontos_perdidos)


    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()