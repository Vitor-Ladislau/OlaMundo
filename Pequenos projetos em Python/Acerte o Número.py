#Tente adivinhar o número com apenas 3 tentativas!

import random

numero = random.randint(1, 10) 
i = 0
print("Tente adivinhar o número de 1 a 10 que eu estou pensando!")

while i < 3:
    i+=1
    tentativa = int(input("Digite um número: "))
    if tentativa != numero:
        print("Você errou tente novamente!")
        if tentativa < numero:
            print("O número que eu estou pensando é um pouco maior!")
        else: 
            print("O número que eu estou pensando é um pouquinho menor!")
    elif tentativa == numero:
        print("Parabéns você")
    if i == 3 and tentativa!= numero:
        print("Já era, você perdeu!")
        print(f"O número era {numero}")