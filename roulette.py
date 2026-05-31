import time
import random
import tools
try:
    from colorama import init
    init()
except:
    try:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    except:
        input('A colorama könyvtár nem települt...')


PIROS = "\033[91m"
FEKETE = "\033[90m"
ZOLD = "\033[92m"
RESET = "\033[0m"

piros_szamok = [
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
]

fekete_szamok = [
    2, 4, 6, 8, 10, 11, 13, 15, 17,
    20, 22, 24, 26, 28, 29, 31, 33, 35
]

osszes_szam = [0] + piros_szamok + fekete_szamok


def szines_szam(szam):

    if szam == 0:
        return f"{ZOLD}● {szam}{RESET}"

    if szam in piros_szamok:
        return f"{PIROS}● {szam}{RESET}"

    return f"{FEKETE}● {szam}{RESET}"


def porges_animacio(eredmeny):

    porgesek = random.randint(60, 100)

    for i in range(porgesek):

        aktualis = random.choice(osszes_szam)

        print(f"\r🎰 Pörög: {szines_szam(aktualis)}", end="")

        time.sleep(0.03 + (i / porgesek) * 0.05)

    print(f"\r🎰 Eredmény: {szines_szam(eredmeny)}       ")


def szam_tet(eredmeny, penz, tet, normal):

    while True:
        valasz = input(
            'Melyik számra szeretnél fogadni?\nVálaszod: '
        ).strip()

        if not valasz.isdigit():
            print('❌ Hibás szám! Kérlek, adj meg egy 0 és 36 közötti számot.')
            continue

        valasz = int(valasz)

        if valasz not in osszes_szam:
            print('❌ Hibás szám! A számnak 0 és 36 közötti értéknek kell lennie.')
            continue

        break

    porges_animacio(eredmeny)

    if valasz == eredmeny:
        print('✅ Nyertél!')
        if normal:
                penz = tools.nyeres6(penz,tet)
        elif not normal:
            penz = tools.nyeres12(penz,tet)
        return penz
    else:
        print('❌ Vesztettél!')
        return penz


def szin_tet(eredmeny, penz, tet, normal):

    while True:
        valasz = input(
            'Melyik színre fogadsz? (piros/fekete)\nVálaszod: '
        ).lower().strip()

        if valasz in ("piros", "fekete"):
            break

        print('❌ Hibás szín! Kérlek, írd be: piros vagy fekete.')

    porges_animacio(eredmeny)

    if valasz == "piros" and eredmeny in piros_szamok:
        print('✅ Nyertél!')
        if normal:
                penz = tools.nyeres2(penz,tet)
        elif not normal:
            penz = tools.nyeres4(penz,tet)
        return penz

    elif valasz == "fekete" and eredmeny in fekete_szamok:
        print('✅ Nyertél!')
        if normal:
                penz = tools.nyeres2(penz,tet)
        elif not normal:
            penz = tools.nyeres4(penz,tet)
        return penz

    else:
        print('❌ Vesztettél!')
        return penz


def paros_paratlan_tet(eredmeny, penz, tet, normal):

    while True:
        valasz = input(
            'Mire fogadsz? (páros/páratlan)\nVálaszod: '
        ).lower().strip()

        if valasz in ("páros", "páratlan"):
            break

        print('❌ Hibás választás! Kérlek, írd be: páros vagy páratlan.')

    porges_animacio(eredmeny)

    if eredmeny == 0:
        print('❌ A 0 sem nem páros, sem nem páratlan!')
        return penz

    elif valasz == "páros" and eredmeny % 2 == 0:
        print('✅ Nyertél!')
        if normal:
                penz = tools.nyeres2(penz,tet)
        elif not normal:
            penz = tools.nyeres4(penz,tet)
        return penz

    elif valasz == "páratlan" and eredmeny % 2 == 1:
        print('✅ Nyertél!')
        if normal:
                penz = tools.nyeres2(penz,tet)
        elif not normal:
            penz = tools.nyeres4(penz,tet)
        return penz

    else:
        print('❌ Vesztettél!')
        return penz


class Jatek:

    def __init__(self, valasz, eredmeny, penz, tet, normal):

        self.valasz = valasz
        self.eredmeny = eredmeny
        self.penz=penz
        self.tet=tet
        self.normal=normal

    def valasztas(self, allapot):
        if self.valasz == 'szám':
            self.penz = szam_tet(self.eredmeny, self.penz, self.tet, self.normal)
            allapot = 1

        elif self.valasz == 'szín':
            self.penz = szin_tet(self.eredmeny, self.penz, self.tet, self.normal)
            allapot = 1

        elif self.valasz == 'pp':
            self.penz = paros_paratlan_tet(self.eredmeny, self.penz, self.tet, self.normal)
            allapot = 1

        else:
            allapot = 0
            input('❌ Hibás választás!')
        
        return allapot


def main(penz, normal):
    while True:
        tools.torles()
        penz, tet = tools.tet(penz)
        if tet == 0:
            break
        

        allapot = 0
        
        while allapot == 0:
            tools.torles()

            print('🟥 ROULETTE 🟦')

            valasz = input(
                'Mire szeretnél fogadni?\n'
                '- szám\n'
                '- szín\n'
                '- pp (páros/páratlan)\n'
                'Válaszod: '
            ).lower()

            eredmeny = random.choice(osszes_szam)

            jatek = Jatek(valasz, eredmeny, penz, tet, normal)
            allapot = jatek.valasztas(allapot)

        penz = jatek.penz
        input('Folytatás...')
    return penz