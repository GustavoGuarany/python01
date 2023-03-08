print ("**************************************")
print ("************Jogo da forca ************")
print ("**************************************")

palavra_secreta = "banana"

enforcou = False
acertou = False

print(not enforcou)

while (not enforcou and not acertou):
    chute = input("Qual a letra? ")
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            print("Letra {} encontrada na posição {}".format(chute,index))
        index = index + 1