import tkinter as tk

def vesztes():
    root = tk.Tk()
    root.attributes("-topmost", True) 
    label = tk.Label(root, text="Vesztes vagy", font=("Arial", 190))
    label.pack()
    root.mainloop()