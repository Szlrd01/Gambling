import random
import os




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