import f1
import fejiras
import slot
import blackjack
import vesztes
import os

def start():
    while True:
        with open('penz.txt', 'r',encoding='utf-8') as f:
            penz = f.read()
        penz=int(penz)
        if penz <= 0:
            vesztes.vesztes()
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('----  Bálint-Akóts Diamond Casino  ----')
            print(f'Egyenleged: {penz}')
            x = input(f'\nMit akarsz játszani?\n(1) Fej vagy írás\n(2) BlackJack\n(3) Slot\n(4) F1 fogadás\n(0) Kilépés\nVálasztásod: ')
            
            if x.isdigit():
                x = int(x)
            elif not x.isdigit():
                None

            if x == 1:
                fejiras.fej_iras(penz)
            elif x == 2:
                blackjack.blackjack(penz)
            elif x == 3:
                slot.slot(penz)
            elif x == 4:
                f1.formula1(penz)
            elif x == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            