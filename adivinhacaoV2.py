import random

print ("**** Jogo de adivinhação *****")

numero_secreto = random.randint(1,100)
pontos = 1000


nivel = int(input("Qual nivel de dificuldade? (1) Facil (2) Medio (3) Dificil: "))
if nivel == 1 :
    numero_tentativas = 5
elif (nivel == 2):
    numero_tentativas = 10
else:
    numero_tentativas = 15


for rodada in range(1,numero_tentativas + 1 ):

    chute = int(input("Digite um numero entre 1 e 100:"))
    if (chute > 100):
        print ("Por favor, digite apenas numeros entre 1 e 100")
        continue
    if (chute < 0):
        print ("Por favor, digite apenas numeros entre 1 e 100")
        continue

    if (chute == numero_secreto):
        print ("Parabens!!! Você acertou e sua pontuação é:", pontos)
        break
    elif(chute > numero_secreto):
        print ("Você digitou um numero maior")
    elif(chute < numero_secreto):
        print ("Você digitou um numero menor")
    tentativas_faltando = numero_tentativas - rodada
    vt = abs(numero_secreto - chute)

    pontos = pontos - vt


    print ("Você tem {} de {} tentativas".format(tentativas_faltando, numero_tentativas))