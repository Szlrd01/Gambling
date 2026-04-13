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
def blackjack():
    while True:
        penz = input('Rakd fel tétet: ')
        if int(penz) > 0:
            x = random.randint(1,10)
            y = random.randint(1,10)
            print(f'A kártyáid: {x} és {y}')  
            print(f'🂼 {y}, {x}')
        elif int(penz) == 0:
            break
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
        x = int(input(f'Mit akarsz játszani?\n(1) Fej vagy írás\n(2) BlackJack\n(3)\n(0) Kilépés\nVálasztásod: '))  
        if x == 1:
            fej_iras(penz)
        elif x == 2:
            blackjack()
        elif x == 3:
            penz=0
        elif x == 0:
            break
        

