def torles():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def vesztes():
    import tkinter as tk
    import sys
    root = tk.Tk()
    root.attributes("-topmost", True)
    
    label = tk.Label(root, text="Vesztes vagy!", font=("Arial", 190))
    label.pack()


    def on_closing():
        root.destroy()  
        sys.exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()


def tet(penz):

    while True:
        print('::: Rakd meg a téteid! :::')
        print(f'Egyenleged: {penz}€')

        tet = input('Rakd fel a tétet: ')

        if not tet.isdigit():
            input('\n❌ Nem számot adtál meg!')
            continue

        tet = int(tet)

        if tet < 0:
            input('\n❌ A tét legyen nagyobb mint 0!')
            continue

        if tet > penz:
            input('\n❌ Nincs elég pénzed!')
            continue
        if tet == 0:
            return penz, tet
        penz -= tet

        return penz, tet


def mentes(penz):
    with open('penz.txt', 'w+',encoding='utf-8') as f:
        f.write(str(penz))


def nyeres2(penz,tet):
    penz=penz+(tet*2)
    return penz
def nyeres4(penz,tet):
    penz=penz+(tet*4)
    return penz

def nyeresslot(penz,tet,jatek):
    if jatek == "cseresznye":
        penz=penz+(tet*2)
    elif jatek == "gyémánt":
        penz=penz+(tet*25)
    elif jatek == "7":
        penz=penz+(tet*100)
    elif jatek == "coin":
        penz=penz+(tet*50)
    elif jatek == "banán":
        penz=penz+(tet*10)
    else:
        pass
    return penz

def nyeresvipslot(penz,tet,jatek):
    if jatek == "cseresznye":
        penz=penz+(tet*4)
    elif jatek == "gyémánt":
        penz=penz+(tet*50)
    elif jatek == "7":
        penz=penz+(tet*200)
    elif jatek == "coin":
        penz=penz+(tet*100)
    elif jatek == "banán":
        penz=penz+(tet*20)
    else:
        pass
    return penz