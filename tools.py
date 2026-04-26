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
