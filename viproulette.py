import time
import random
import tools

def game(penz):
    red, black, green = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35], [0]

    game_still_going = True
    broke = False
    colour_choice = ""
    roll_result = ""
    win_red = False
    win_green = False
    win_black = False
    lose = False
    bank = penz
    betamount = 0
    resulting_number = None


    def intro():
        tools.torles()
        global bank
        print('ROULETTE\n')
        time.sleep(2)
        bank = penz
        tools.torles()

    def display_table():
        print("Roulette Asztal")
        print("Piros: ")
        print(red)
        print("Fekete:")
        print(black)
        print("Zöld:")
        print(green)

    def handle_turn():
        global colour_choice
        global betamount
        global bank
        betamount = 0
        while betamount == 0:
        
            try:
                print(f'Egyenleged: {penz}')
                betamount = int(input('Add meg a tétet: '))
            except ValueError:
                print('\Rossz értéket adtál meg!')
        if betamount > bank:
            betamount = bank
        if bank > betamount:
            bank = bank - betamount
        print("€" + str(betamount))
        colour_choice = (input("Piros(P), Fekete(F), vagy Zöld(Z)? :"))
        if colour_choice == 'p':
            print(f"€ {str(betamount)} van a piros színen!")
        elif colour_choice == 'f':
            print(f"€ {str(betamount)} van a fekete színen!")
        elif colour_choice == 'z':
            print(f"€ {str(betamount)} van a zöld színen!")
        time.sleep(0.5)

    def roll_ball():
        global roll_result
        global resulting_number
        resulting_number = random.randint(0, 35)
        if resulting_number in red:
            roll_result = "piros"
        elif resulting_number in black:
            roll_result = "fekete"
        elif resulting_number in green:
            roll_result = "zöld"
        print(roll_result, resulting_number)

    def check_win():
        global win_black
        global win_red
        global win_green
        global lose
        win_red = False
        win_green = False
        win_black = False
        lose = False
        if colour_choice == "p" and roll_result == "piros":
            win_red = True
            print("Piros nyert!")
            input('...')
        elif colour_choice == "f" and roll_result == "fekete":
            win_black = True
            print("Fekete nyert!")
            input('...')
        elif colour_choice == "z" and roll_result == "zöld":
            win_green = True
            print("Zöld nyert!!")
            input('...')
        else:
            lose = True
            print("Vesztettél!")
            input('...')

    def check_if_broke():
        tools.torles()
        global broke
        if bank < 1:
            broke = True
            print("Elfogyott a pénzed!")
        else:
            pass

    def increment_bank():
        global bank
        if win_red == True:
            bank = bank + (betamount * 5)
        elif win_black == True:
            bank = bank + (betamount * 5)
        elif win_green == True:
            bank = bank + (betamount * 350)
        elif lose == True:
            bank = bank - betamount
        print(bank)

    def play_game():
        handle_turn()
        roll_ball()
        check_win()
        increment_bank()
        check_if_broke()

    intro()
    display_table()
    while game_still_going:
        play_game()
        if broke == True:
            break
        if input(f"Folytatod?\nIgen vagy Nem?\n").strip().upper() != 'IGEN':
            break    
    
    return penz