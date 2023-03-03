print("**********************************")
print("Bem vindo ao jogo de adivinhação!!")
print("**********************************")

numero_secreto = 42
numero_tentativas = 4


for rodada in range(1 , numero_tentativas + 1 ):

    chute_str = input("Digite um número de 1 a 100:")
    print ("Você digitou o numero: ", chute_str)
    print ("Numero de tentativas: {} de {}" .format(rodada , numero_tentativas))
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero de 1 a 100")
        continue

    if (acertou):
        print ("Você acertou")
        break
    else:
        if(maior):
            print("Você chutou um numero maior!")
        elif(menor):
            print ("Você chutou um numero menor!")



print("Fim do jogo")