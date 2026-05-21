import os
import tkinter as tk
import sys

def torles():
    os.system('cls' if os.name == 'nt' else 'clear')

def vesztes():
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
    print(f'Egyenleged: {penz}')
    def levon(penz):
        tet = input('Rakd fel a tétet: ')
        while True:
            tet = input('Rakd fel a tétet: ')
            if tet.isdigit():
                tet = int(tet)
                break
            else:
                pass
        return tet           
        
    if tet <= 0:
        penz=penz-tet
        return penz
    if tet > penz and penz != 0:
        print(f'Egyenleged: {penz}')
        print('Nincs elég pénzed!')
        input('Enter...')
