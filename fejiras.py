import random
import tools

def fej_iras(penz):
    
    try:
        tools.torles()
        penz, tet = tools.tet(penz)
        tools.torles()
        while True:
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
                tools.torles()
                break
            else:
                print("Érvénytelen választás!")
        with open('penz.txt', 'w+') as f:
            f.write(str(penz))
    except ValueError:
        print('Az általad megadott érték nem szám formátumú - lásd: tét')