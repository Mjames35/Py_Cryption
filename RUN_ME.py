import tkinter as tk
from tkinter import *
root = tk.Tk()
from EncryptionFunctions import decryptFunc
from EncryptionFunctions import EncryptFunc
global keyword
keyword = ""

def runE():
    EncryptFunc(keyword)

def runD():
    DecryptFunc(keyword)

def savekword():
    keyword = e.get()



Encrypt = tk.Button(root, text="Encrypt", padx=10, pady=5, fg="white", bg="black", command=runE)
Decrypt = tk.Button(root, text="Decrypt", padx=10, pady=5, fg="white", bg="black", command=runD)
e = Entry(root, width=30, )
inpkword = tk.Button(root, text="Input Keyword", padx=10, pady=5, fg="white", bg="black", command=savekword)

inpkword.pack()
Encrypt.pack()
Decrypt.pack()
e.pack()

root.mainloop()




