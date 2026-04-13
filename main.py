import random
import os
import tkinter as tk

penz = 1000

def fej_iras(penz):
    penz=int(penz)
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print(f'Egyenleged: {penz}')
        tet = int(input('Add meg a tétet: '))
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
def blackjack(penz):
    penz=int(penz)
    def jatek():
        while True:
        
            tet = int(input('Rakd fel tétet: '))
            if tet > 0:
                penz-=tet
                x = random.randint(1,10)
                y = random.randint(1,10)
                kartyak = [x,y]
                print(f'A kártyáid: {x}🂼 és {y}🂼')  
                huz = input('Szeretnél húzni?\n')
                if huz == 'igen':
                    huz = True
                else:
                    huz = False
                    print('akkor nem húzol')
                if huz == True:
                    kartyak.append(random.randint(1,10))
                    print(f'A kártyáid: {kartyak}')
                    ertek = 0
                    for kartya in kartyak:
                        ertek+=kartya
                if ertek == 21:
                    penz+=tet*2
                    print('Nyertél!')
                else:
                    print('Vesztettél!')
                    break
                            
            elif int(penz) == 0:
                break
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Egyenleged: {penz}')
    jatek()
    while True:
        folytat = input('Szeretnéd folytatni?')
        if folytat == 'igen':
            jatek()
            

def slot():
    pass

def formula1():
    pass

def vesztes():
    root = tk.Tk()
    root.attributes("-topmost", True) 
    label = tk.Label(root, text="Vesztes vagy", font=("Arial", 190))
    label.pack()
    root.mainloop()
    
while True:
    with open('penz.txt', 'r',encoding='utf-8') as f:
        penz = f.read()
    penz=int(penz)
    if penz <= 0:
        vesztes()
        
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----  Akóts Bálint Kaszinó  ----')
        print(f'Egyenleged: {penz}')
        x = int(input(f'Mit akarsz játszani?\n(1) Fej vagy írás\n(2) BlackJack\n(3) Slot\n(4) F1 fogadás\n(0) Kilépés\nVálasztásod: '))  
        if x == 1:
            fej_iras(penz)
        elif x == 2:
            blackjack(penz)
        elif x == 3:
            slot()
        elif x == 4:
            formula1()
        elif x == 0:
            break