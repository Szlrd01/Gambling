import random
import os
import tkinter as tk
import time


def fej_iras(penz):
    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')    
        penz=int(penz)
        while True:
            print(f'Egyenleged: {penz}')
            tet = int(input('Add meg a tétet: '))
            if tet == 0:
                break
            penz-=tet
            print("Fej vagy írás játék!")
            print("Írj be: fej vagy írás | 0 - kilépés")
            valasztas = input("A választásod: ").lower()
            gep = random.choice(["fej", "írás"])
            print(f"A gép dobása: {gep}")

            if valasztas == gep:
                        penz+=tet*2
                        print("Eltaláltad! ")
                        
            elif valasztas in ["fej", "írás"]:
                        penz-=tet
                        print("Nem találtad el ")

            elif valasztas == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("Érvénytelen választás!")
        with open('penz.txt', 'w+',encoding='utf-8') as f:
            f.write(str(penz))
    except ValueError:
        print('Az általad megadott érték nem szám formátumú - lásd: tét')

def blackjack(penz):
    penz = int(penz)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Egyenleged: {penz}')

        tet = int(input('Rakd fel a tétet: '))
        if tet <= 0:
            break
        if tet > penz:
            print('Nincs elég pénzed!')
            input('Enter...')
            continue

        penz -= tet

        player_kartyak = [random.randint(1, 10), random.randint(1, 10)]
        dealer_kartyak = [random.randint(1, 10), random.randint(1, 10)]

        while True:
            player_osszeg = sum(player_kartyak)
            print(f'\nA kártyáid: {player_kartyak} (összeg: {player_osszeg})')

            if player_osszeg > 21:
                print('Túllépted a 21-et! Vesztettél.')
                break

            huz = input('Húzol? (igen/nem): ').lower().strip()
            if huz == 'igen':
                player_kartyak.append(random.randint(1, 10))
            else:
                break

        if sum(player_kartyak) > 21:
            input('Enter...')
            continue

        print(f'\nDealer lapjai: {dealer_kartyak}')
        while sum(dealer_kartyak) < 17:
            dealer_kartyak.append(random.randint(1, 10))

        dealer_osszeg = sum(dealer_kartyak)
        player_osszeg = sum(player_kartyak)

        print(f'Dealer végső lapjai: {dealer_kartyak} (osszeg: {dealer_osszeg})')

        if dealer_osszeg > 21 or player_osszeg > dealer_osszeg:
            print('Nyertél!')
            penz += tet * 2
        elif player_osszeg == dealer_osszeg:
            print('Döntetlen!')
            penz += tet
        else:
            print('Vesztettél!')

        input('Enter...')

    print(f'Kiléptél. Végső egyenleg: {penz}')
    with open('penz.txt', 'w+',encoding='utf-8') as f:
            f.write(str(penz))
    
def slot(penz):
    penz = int(penz)
    ikonok = ['💎','🍒','7️⃣','🪙','🍌']
    gy_db = 0
    cs_db = 0
    h_db = 0
    c_db = 0
    b_db = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print(f'Egyenleged: {penz}')
        tet = int(input('Rakd fel a tétet: '))
        
        if tet <= 0:
            break
        if tet > penz and penz != 0:
            print(f'Egyenleged: {penz}')
            print('Nincs elég pénzed!')
            input('Enter...')
            continue
        penz=penz-tet
        while True:
            a = ikonok[random.randint(0,4)]
            b = ikonok[random.randint(0,4)]
            c = ikonok[random.randint(0,4)]
            eredmeny = [a,b,c]
            gy_db = eredmeny.count('💎')
            cs_db = eredmeny.count('🍒')
            h_db = eredmeny.count('7️⃣')
            c_db = eredmeny.count('🪙')
            b_db = eredmeny.count('🍌')
            


            for i in range(5):
                os.system('cls' if os.name == 'nt' else 'clear')
                print('SLOT MACHINE')
                print(f'|\t{ikonok[random.randint(0,4)]}\t|\t{ikonok[random.randint(0,4)]}\t|\t{ikonok[random.randint(0,4)]}\t|')
                time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('SLOT MACHINE')
            
            
            


            print(f'|\t{a}\t|\t{b}\t|\t{c}\t|')
            if a == '💎' and b == '💎' and c == '💎':
                penz=penz+tet*25
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '7️⃣' and b == '7️⃣' and c == '7️⃣':
                penz=penz+tet*100
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '🍒' and b == '🍒' and c == '🍒':
                penz=penz+tet*2
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '🪙' and b == '🪙' and c == '🪙':
                penz=penz+tet*50
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '🍌' and b == '🍌' and c == '🍌':
                penz=penz+tet*10
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif gy_db == 2 or cs_db == 2 or h_db == 2 or c_db == 2 or b_db == 2:
                penz=penz+tet*5
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            else:
                print('Sajnos nem nyertél!')
                input('Enter...')
                break
    with open('penz.txt', 'w+',encoding='utf-8') as f:
            f.write(str(penz))
    return penz

def formula1():
    pass
def roulett():
    pass


def vesztes():
    root = tk.Tk()
    root.attributes("-topmost", True) 
    label = tk.Label(root, text="Vesztes vagy", font=("Arial", 190))
    label.pack()
    root.mainloop()

os.system('cls' if os.name == 'nt' else 'clear')
with open('penz.txt', 'r',encoding='utf-8') as f:
        penz = f.read() 
        penz = int(penz)
if penz == 1000:
    pass
else:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        reset = input(f'Szeretnéd resetelni az egyenleged? ({penz})\nigen/nem: ')
        if reset == 'igen':
            with open('penz.txt', 'w+',encoding='utf-8') as f:
                f.write('1000')
            break
        elif reset == 'nem': 
            break
        else:
            pass

while True:
    with open('penz.txt', 'r',encoding='utf-8') as f:
        penz = f.read()
    penz=int(penz)
    if penz <= 0:
        vesztes()
        
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----  Bálint-Akóts Diamond Casino  ----')
        print(f'Egyenleged: {penz}')
        x = int(input(f'Mit akarsz játszani?\n(1) Fej vagy írás\n(2) BlackJack\n(3) Slot\n(4) F1 fogadás\n(0) Kilépés\nVálasztásod: '))  
        if x == 1:
            fej_iras(penz)
        elif x == 2:
            blackjack(penz)
        elif x == 3:
            slot(penz)
        elif x == 4:
            formula1()
        elif x == 0:
            break