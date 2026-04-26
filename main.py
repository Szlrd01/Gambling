import os
import app
import sys

def main(penz):
    if penz is None:
        sys.exit()
    if penz < 1000:
        penz = reset(penz)
        if penz is None:
            sys.exit()
    app.start()   

def torles():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset(penz):
    while True:
        torles()
        res = input(f'Szeretnéd újratölteni az egyenleged? ({penz})\nigen/nem: ').strip().lower()
        if res == 'igen':
            penz = 1000
            with open('penz.txt', 'w') as f:
                f.write(str(penz))
            return penz
        elif res == 'nem':
            torles()
            return None
        else:
            input('Hibás bemenet...')


try:
    with open('penz.txt', 'r') as f:
        penz=f.readline().strip()

    penz=int(penz)
except ValueError:
    torles()
    print('A pénz rossz formátumban lett megadva!')
    input('\nEnter a folytatáshoz...')
    penz = reset(0)
except FileNotFoundError:
    with open('penz.txt', 'w') as f:
        penz=1000
        f.write(str(penz))

main(penz)