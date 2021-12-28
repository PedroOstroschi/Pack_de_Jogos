import random
def show_game_name():
    nome_do_jogo = "Jogo da forca"
    print("Bem vindo ao " + nome_do_jogo)

def initialize_keyword():
    file = open("words.txt", "r")
    fruits = [line.strip() for line in file]
    file.close()
    number = random.randrange(0, len(fruits))
    return fruits[number]


def initialize_right_letters(key_word):
    return ["_" for letter in key_word]



def get_user_answer():
    return input("insira letra: ").lower().strip()

def save_right_letters(user_answer, right_letters, key_word):
    index = 0
    for letter in key_word:
        if (user_answer == letter):
            right_letters[index] = letter
            print("Encontrei {} na posição {}.".format(letter, index))
        index += 1

def loss_screen(key_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(key_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def win_screen():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def draw(life):
    print("  _______     ")
    print(" |/      |    ")

    if(life == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(life == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(life == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(life == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(life == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(life == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (life == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def run():
    show_game_name()

    #initialized variables
    hanged = False
    win = False
    life = 8
    key_word = initialize_keyword()
    right_letters = initialize_right_letters(key_word)

    while( not hanged and not win):
        win = "_" in right_letters
        user_answer = get_user_answer()
        if key_word.find(user_answer) < 0:
            print("Errou!")
            life -= 1

        else:
            save_right_letters(user_answer,right_letters,key_word)

        win = "_" not in right_letters
        hanged = life == 0
        draw(life)
        print(right_letters)


    if win: win_screen()
    else:loss_screen(key_word)
