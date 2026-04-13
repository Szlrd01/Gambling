import random
import os
def fej_iras():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fej vagy írás játék!")
        print("Írj be: fej vagy írás | 0 - kilépés")
        valasztas = input("A választásod: ").lower()
        gep = random.choice(["fej", "írás"])
        print(f"A gép dobása: {gep}")

        if valasztas == gep:
            print("Eltaláltad! ")
        elif valasztas in ["fej", "írás"]:
            print("Nem találtad el ")
        elif valasztas == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Érvénytelen választás!")
            
    
    

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    x = int(input(f'Mit akarsz játszani?\n(1) Fej vagy írás\n(2)\n(3)\nVálasztásod: '))
    if x == 1:
        fej_iras()
    elif x == 0:
        break