import random
import tools

def fej_iras(penz):
    while True:
        tools.torles()
        penz, tet = tools.tet(penz)
        if tet == 0:
            break
        tools.torles()
        gep = random.choice(["fej", "írás"])        
        while True:
            print("🪙 Fej vagy Írás? 🪙\n")
            print("(fej / írás / 0 - kilépés)")
            valasztas = input("Választásod: ").lower()

            if valasztas == gep:
                print(f"\nA gép dobása: {gep}")
                penz+=tet*2
                print("Eltaláltad!")
                input('Enter...')
                break
                            
            elif valasztas in ["fej", "írás"]:
                print(f"\nA gép dobása: {gep}")
                penz-=tet
                print("Nem találtad el!")
                input('Enter...')
                break

            elif valasztas == '0':
                penz+=tet
                tools.torles()
                break
            else:
                input('Érvénytelen választás!')
                tools.torles()
        
    tools.mentes(penz)
    return penz