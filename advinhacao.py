import math
import random

def run():
    #game name
    nome_do_jogo = "Jogo de Adivinhação"
    print("Bem vindo ao " + nome_do_jogo)

    key = random.randrange(0, 101)
    user_answer = ""
    points = 1000
    nivel = int(input("Qual o nível de dificuldade? 1  2  3: "))

    if(nivel == 1):
        max_try=20
    elif(nivel == 2):
        max_try=10
    else:
        max_try = 5

    for round in range(0, max_try):

        user_answer_str = input("digite seu  entre 1 e 100 ou sair: " )
        if(user_answer_str == "sair"): break
        try:
            user_answer = int(user_answer_str)
        except:
            print("Digite um número de 1 a 100!")

        if(user_answer < 1 or user_answer > 100): print("Apenas números de 1 a 100")

        win = user_answer == key
        if (win):
            print("Acertou, pontos: {}!".format(points))
            break
        elif (int(user_answer) > key):
            print("Tente um número menor.")
            delta = abs(key - user_answer)
            points = points - delta
        else:
            print("Tente um número maior.")
            delta = abs(key - user_answer)
            points = points - delta

    print("Fim")
