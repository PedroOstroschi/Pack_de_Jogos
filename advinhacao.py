import math
import random
def show_game_name():
    nome_do_jogo = "Jogo de Adivinhação"
    print("Bem vindo ao " + nome_do_jogo)

def initialize_key():
    return random.randrange(0, 101)

def get_difficulty():
    nivel = int(input("Qual o nível de dificuldade? 1  2  3: "))

    if (nivel == 1):
        return 20
    elif (nivel == 2):
        return 10
    else:
        return 5

def get_user_answer():
    return input("digite seu  entre 1 e 100 ou sair: " )


def run():

    show_game_name()

    #initialize variables
    key = initialize_key()
    user_answer = ""
    points = 1000
    max_try = get_difficulty()

    for round in range(0, max_try):

        user_answer_str = get_user_answer()
        sair = user_answer_str == "sair"

        if(sair): break
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
