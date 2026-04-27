import f1
import fejiras
import slot
import blackjack
import tools
import roulette
import ecasino

def start():
    with open('penz.txt', 'r') as f:
            penz = f.read()
            penz=int(penz)
    while True:
        if penz <= 0:
            tools.vesztes()  
        else:
            tools.torles()
            print('----  Bálint-Akóts Diamond Casino  ----')
            print(f'Egyenleged: {penz}')
            x = input(f'\nMit akarsz játszani?\n(1) Fej vagy írás\n(2) BlackJack\n(3) Slot\n(4) F1 fogadás\n(5) Roulette\n\n(e) VIP Casino\n(x) Mentés\n(0) Kilépés\nVálasztásod: ')
            
            if x.isdigit():
                x = int(x)
            elif not x.isdigit():
                None

            if x == 'x':
                with open('penz.txt', 'w') as f:
                    f.write(str(penz))
                input('Mentve...')
            elif x == 'e':
                penz = ecasino.start(penz)

            if x == 1:
                penz = fejiras.fej_iras(penz)
            elif x == 2:
                penz = blackjack.blackjack(penz)
            elif x == 3:
                penz = slot.slot(penz)
            elif x == 4:
                penz = f1.formula1(penz)
            elif x == 5:
                penz= roulette.game(penz)
            elif x == 0:
                
                tools.torles()
                break

    with open('penz.txt', 'w') as f:
        f.write(str(penz))
    return penz