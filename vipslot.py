import random
import tools
import time

def slot(penz):
    penz = int(penz)
    if penz > 5:
        pass
    ikonok = ['💎','🍒','7️⃣','🪙','🍌']
    gy_db = 0
    cs_db = 0
    h_db = 0
    c_db = 0
    b_db = 0

    tools.torles()
    while True:
        print(f'Egyenleged: {penz}')
        tet = int(input('Rakd fel a tétet: '))
        
        if tet <= 0:
            break
        if tet > penz and penz != 0:
            print(f'Egyenleged: {penz}')
            print('Nincs elég pénzed!')
            input('Enter...')
            continue
        penz=penz-tet
        while True:
            a = ikonok[random.randint(0,4)]
            b = ikonok[random.randint(0,4)]
            c = ikonok[random.randint(0,4)]
            eredmeny = [a,b,c]
            gy_db = eredmeny.count('💎')
            cs_db = eredmeny.count('🍒')
            h_db = eredmeny.count('7️⃣')
            c_db = eredmeny.count('🪙')
            b_db = eredmeny.count('🍌')
            


            for i in range(7):
                tools.torles()
                print('SLOT MACHINE')
                print(f'|\t{ikonok[random.randint(0,4)]}\t|\t{ikonok[random.randint(0,4)]}\t|\t{ikonok[random.randint(0,4)]}\t|')
                time.sleep(0.5)
            tools.torles()
            print('SLOT MACHINE')
            
            
            


            print(f'|\t{a}\t|\t{b}\t|\t{c}\t|')
            if a == '💎' and b == '💎' and c == '💎':
                penz=penz+tet*50
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '7️⃣' and b == '7️⃣' and c == '7️⃣':
                penz=penz+tet*200
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '🍒' and b == '🍒' and c == '🍒':
                penz=penz+tet*4
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '🪙' and b == '🪙' and c == '🪙':
                penz=penz+tet*100
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif a == '🍌' and b == '🍌' and c == '🍌':
                penz=penz+tet*20
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            elif gy_db == 2 or cs_db == 2 or h_db == 2 or c_db == 2 or b_db == 2:
                penz=penz+tet*10
                print(f'Egyenleged: {penz}')
                print('Gratulálok, nyertél!')
                input('Enter...')
                break
            else:
                print('Sajnos nem nyertél!')
                input('Enter...')
                break
    with open('penz.txt', 'w',encoding='utf-8') as f:
            f.write(str(penz))
    return penz