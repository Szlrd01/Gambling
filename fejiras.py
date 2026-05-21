import random
import tools

def fej_iras(penz):
    while True:
        tools.torles()
        penz, tet = tools.tet(penz)
        if tet == 0:
            break
        tools.torles()
        print("::: Fej vagy Írás? :::")
        print("(fej / írás / 0 - kilépés)")
        valasztas = input("Választásod: ").lower()
        gep = random.choice(["fej", "írás"])
        print(f"\nA gép dobása: {gep}")

        if valasztas == gep:
            penz+=tet*2
            print("Eltaláltad!")
            input('Enter...')
                        
        elif valasztas in ["fej", "írás"]:
            penz-=tet
            print("Nem találtad el!")
            input('Enter...')

        elif valasztas == '0':
            tools.torles()
            break
        else:
            print("Érvénytelen választás!")
    tools.mentes(penz)
    return penz