import tkinter as tk
from tkinter import *
root = tk.Tk()

def runE():
    import Encryption.py   
def runD():
    import Decryption.py


Encrypt = tk.Button(root, text="Encrypt", padx=10, pady=5, fg="white", bg="black", command=runE)
Decrypt = tk.Button(root, text="Decrypt", padx=10, pady=5, fg="white", bg="black", command=runD)
Encrypt.pack()
Decrypt.pack()

root.mainloop()
