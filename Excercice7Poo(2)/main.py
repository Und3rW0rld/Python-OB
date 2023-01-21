class Alumno:
    nombre = None
    nota = None
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimirResultado(self):
        print("El alumno se llama:", self.nombre)
        if(int(self.nota) >= 7):
            print("El alumno ha aprobado con la nota:", self.nota)
        else: print("El alumno no ha aprobado con la nota:", self.nota)
#Suponemos que se aprueba con una nota mayor o igual a 7
def Main():
    estudiante = Alumno ("Pepito", 4)
    estudiante.imprimirResultado()
if __name__ == '__main__':
    Main()