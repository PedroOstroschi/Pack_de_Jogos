import advinhacao
import forca

def choose_game():
    jogo = 0

    try:
        jogo = int(input("Selecine um jogo (1) Advinhação (2) Forca: "))
        if (jogo == 1):
            advinhacao.run()
        elif (jogo == 2):
            forca.run()
    except:
        print("Digite um NUMERO 1 ou 2, animal!")




if(__name__ == "__main__"):
    choose_game()