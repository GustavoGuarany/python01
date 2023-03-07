import random

print ("**** Jogo de adivinhação *****")


pontos = 1000
facil = random.randint(1,10)
medio = random.randint(1,40)
dificil = random.randint(1,100)

rodada = 0
numero_tentativas = 5


nivel = int(input("Qual nivel de dificuldade? (1) Facil (2) Medio (3) Dificil: "))
if nivel == 1 :
    chute = int(input("Digite um numero entre 1 e 10:"))
    aleatorio = facil
    numero_tentativas = 4

elif (nivel == 2):
    chute = int(input("Digite um numero entre 1 e 40:"))
    aleatorio = medio
    numero_tentativas = 8
else:
    chute = int(input("Digite um numero entre 1 e 100:"))
    aleatorio = dificil
    numero_tentativas = 12

print(aleatorio)

for rodada in range(1,numero_tentativas + 1 ):
    if chute == aleatorio:
        print("Parabens você acertou!!! Sua pontuação é {}" .format(pontos))
        break
    elif chute != aleatorio:
        print("Você errou!!")
        rest_tentativa = numero_tentativas - rodada
        vt = abs(chute - aleatorio)
        print(vt)
        pontos = pontos - vt
        print(pontos)

        print("Restam {} tentativas".format(rest_tentativa))
        chute = int(input("Tente novamente, digite outro numero: "))


import random

print ("**** Jogo de adivinhação *****")


pontos = 1000
facil = random.randint(1,10)
medio = random.randint(1,40)
dificil = random.randint(1,100)

rodada = 0
numero_tentativas = 5


nivel = int(input("Qual nivel de dificuldade? (1) Facil (2) Medio (3) Dificil: "))
if nivel == 1 :
    chute = int(input("Digite um numero entre 1 e 10:"))
    aleatorio = facil
    numero_tentativas = 4

elif (nivel == 2):
    chute = int(input("Digite um numero entre 1 e 40:"))
    aleatorio = medio
    numero_tentativas = 8
else:
    chute = int(input("Digite um numero entre 1 e 100:"))
    aleatorio = dificil
    numero_tentativas = 12

print(aleatorio)

for rodada in range(1,numero_tentativas + 1 ):
    if chute == aleatorio:
        print("Parabens você acertou!!! Sua pontuação é {}" .format(pontos))
        break
    elif chute > aleatorio:
        print("Você errou!! Tente um numero menor")
    elif chute < aleatorio:
        print("Você errou!! Tente um numero maior")
        rest_tentativa = numero_tentativas - rodada
        if (aleatorio == facil):
            vt = abs(chute - aleatorio) * 20
            pontos = pontos - vt
        elif (aleatorio == medio):
            vt = abs(chute - aleatorio) * 10
            pontos = pontos - vt
        else:
            vt = abs(chute - aleatorio)
            pontos = pontos - vt
        print(pontos)

        print("Restam {} tentativas".format(rest_tentativa))
        chute = int(input("Tente novamente, digite outro numero: "))
