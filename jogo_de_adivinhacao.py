import random

print("Bem vindo ao jogo de advinhação!")
numero_secreto = random.randrange(1, 101)
tentativas = 0
pontos = 100

print("Qual é o nível de dificuldade que você quer?")
print("{1} Fácil {2} Médio {3} Difícil")
nivel = int(input("Defina o nível:"))

if nivel == 1:
    tentativas = 20
elif nivel == 2:
    tentativas = 5
elif nivel == 3:
    tentativas = 3

while tentativas > 0:
    print("Você tem mais", tentativas, "tentativas.")
    chute = int(input("Adivinhe o número:"))
    print("Você escolheu o número", chute, "?")
    
    if chute < 1 or chute > 100:
        print("Você deve escolher um número de 1 a 100")
        continue 
    
    if chute == numero_secreto:
        print("Você acertou e fez", pontos, "pontos!")
        break
    else:
        if chute > numero_secreto:
            print("Você chutou alto.")
        else:
            print("Você chutou baixo.")
            
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos
        tentativas -= 1

print("Fim de jogo!")
