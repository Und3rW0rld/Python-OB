from tkinter import *
raiz = Tk()
listbox = Listbox(raiz)
lista = ["Pepe", "Juanito", "Sebastián",  "Sofía"]
for item in lista:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Este es el texto opcional")
label.pack()
raiz.mainloop()