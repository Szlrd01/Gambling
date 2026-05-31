import f1
import fejiras
import slot
import blackjack
import tools
import roulette
import vip


def start():
    with open('penz.txt', 'r') as f:
            penz = f.read()
            penz=int(penz)
    while True:
        normal = True
        if penz <= 0:
            tools.vesztes()  
        else:
            tools.torles()
            print('----  Bálint-Akóts Diamond Casino  ----')
            print(f'::: Egyenleged: {penz}€ :::')
            print(f'\nMit szeretnél játszani?\n(1) Fej vagy írás\n(2) BlackJack\n(3) Slot\n(4) F1 fogadás\n(5) Roulette\n\nTovábbi lehetőségek:\n(e) VIP Casino\n(x) Mentés\n(0) Kilépés\n')
            x = input('Választásod: ')
            
            if x.isdigit():
                x = int(x)
            elif not x.isdigit():
                None

            if x == 'x':
                with open('penz.txt', 'w') as f:
                    f.write(str(penz))
                input('Mentve...')
            elif x == 'e':
                tools.mentes(penz)
                penz = vip.start(penz)

            if x == 1:
                penz = fejiras.fej_iras(penz)
            elif x == 2:
                penz = blackjack.blackjack(penz, normal)
            elif x == 3:
                penz = slot.slot(penz,normal)
            elif x == 4:
                penz = f1.formula1(penz)
            elif x == 5:
                penz= roulette.main(penz, normal)
            elif x == 0:
                
                tools.torles()
                break

    with open('penz.txt', 'w') as f:
        f.write(str(penz))
    return penz