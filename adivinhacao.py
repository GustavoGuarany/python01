print("**********************************")
print("Bem vindo ao jogo de adivinhação!!")
print("**********************************")

numero_secreto = 42
numero_tentativas = 4
rodada = 1

while (rodada < numero_tentativas):

    chute_str = input("Digite o seu numero: ")
    print ("Você digitou o numero: ", chute_str)
    print ("Numero de tentativas:",rodada ,"de" , numero_tentativas)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if (acertou):
        print ("Você acertou")
    else:
        if(maior):
            print("Você chutou um numero maior!")
        elif(menor):
            print ("Você chutou um numero menor!")

    rodada = rodada + 1

print("Fim do jogo")