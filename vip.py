import tools
import blackjack
import slot
import roulette

def start(penz):
    normal = False
    while True:
        try:
            with open('ticket.txt','r') as t:
                ticket = t.readline()
                ticket = int(ticket)
        except:
            with open('ticket.txt','w') as t:
                ticket=0
                t.write(str(ticket))
                

        if ticket == 0:
            input('Jegyet kell vásárolnod...')
            x = input('Veszel jegyet? (igen/nem)\nÁra: 5000€ | Válaszod: ')
            if x == 'igen':
                if penz > 5000:
                    penz=penz-5000
                    input('\n✅ Sikeres vásárlás!')
                else:
                    input('\n❌ Nincs elég pénzed!')
                    return penz               
                with open('penz.txt','w+') as f:
                    f.write(str(penz))
                ticket = 1
                with open('ticket.txt','w+') as t:
                    t.write(str(ticket))
            else:
                return penz
        elif ticket == 1:
            pass
                    
        if penz < 10000:
            input('10000€-nak kell lennie az egyenlegeden!')
            return penz
        
        else:
            break                                                    
    
    with open('penz.txt', 'r') as f:
            penz = f.read()
            penz=int(penz)
    while True:
        if penz <= 0:
            tools.vesztes()  
        else:
            tools.torles()
            print('---- 🏅 VIP RÉSZLEG 💎 ----')
            print(f'::: Egyenleged: {penz}€ :::')
            x = input(f'\nMit szeretnél játszani?\n(1) BlackJack\n(2) Slot\n(3) Roulette\n\n(x) Mentés\n(0) Kilépés\nVálasztásod: ')
            
            if x.isdigit():
                x = int(x)
            elif not x.isdigit():
                None

            if x == 'x':
                with open('penz.txt', 'w') as f:
                    f.write(str(penz))
                input('Mentve...')
            


            if x == 1:
                penz = blackjack.blackjack(penz, normal)
            elif x == 2:
                penz = slot.slot(penz, normal)
            elif x == 3:
                penz = roulette.main(penz, normal)
            elif x == 0:
                tools.torles()
                break

    tools.mentes(penz)
    return penz