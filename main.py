import os
import app

def reset(penz):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            res = input(f'Szeretnéd resetelni az egyenleged? ({penz})\nigen/nem: ')
            if res == 'igen':
                penz = 1000
                with open('penz.txt', 'w+',encoding='utf-8') as f:
                    f.write(str(penz))
                break
            elif res == 'nem': 
                if not penz.isdigit():
                     penzerror(penz)
                else:
                    break
            else:
                pass
    return penz
    
def penzerror(penz):
    print('A pénz rossz formátumban lett megadva!')
    input('Enter...')
    reset(penz)    
        


 
def roulett():
    pass



with open('penz.txt', 'r',encoding='utf-8') as f:
        penz = f.read() 
        
if penz.isdigit():
    penz = int(penz)
    if penz > 999:
        app.start()
    elif penz < 1000:
        reset(penz)
else:
    penzerror(penz)





