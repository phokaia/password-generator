import string
import pyperclip
from random import *
from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("Password Generator")
pencere.geometry("500x200")

uygulama = Frame(pencere)
uygulama.pack()

def olustur():
    chars = string.ascii_letters + string.digits + string.punctuation
    length = E1.get()
    sifre = "".join(choice(chars) for x in range(randint(int(length),int(length))))
    L3.config(text=sifre)
    pyperclip.copy(sifre)
    messagebox.showinfo("Uyarı" , "Şifreniz panoya kopyalandı!")

baslik = Label(uygulama, text="Şifre Oluşturucu", font="bold", fg="red")
baslik.grid(row=0, column=1, pady="10")

L1 = Label(uygulama, text="Şifre uzunluğu girin :")
L1.grid(row=1, column=0)

E1 = Entry(uygulama)
E1.grid(row=1, column=1)
E1.focus()
E1.bind("<Return>",olustur)

B1 = Button(uygulama, text="Oluştur", command=olustur)
B1.grid(row=1, column=2, padx="5")

L2 = Label(uygulama, text="Şifreniz :")
L2.grid(row=2, column=0)

L3 = Label(uygulama, text="", font="bold")
L3.grid(row=2, column=1, pady="20")

pencere.mainloop()