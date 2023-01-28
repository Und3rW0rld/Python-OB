from tkinter import *
def seleccionar():
    monitor.config(text=f'{opcion.get()}')
def reset():
    opcion.set(None)
    monitor.config(text="")
raiz = Tk()
raiz.title("Vamos a seleccionar!")
opcion = StringVar()
opcion.set(None)
Radiobutton(raiz, text="Patata", variable=opcion, value='Patata', command=seleccionar).pack(anchor=W)
Radiobutton(raiz, text="Salpicon", variable=opcion, value='Salpicon', command=seleccionar).pack(anchor=W)
Radiobutton(raiz, text="Empanada", variable=opcion, value='Empanada', command=seleccionar).pack(anchor=W)
Radiobutton(raiz, text="Chocolate", variable=opcion, value='Chocolate', command=seleccionar).pack(anchor=W)
monitor = Label(raiz)
monitor.pack()
Button(raiz, text="Reinicio", command=reset, bg="blue").pack()
raiz.mainloop()