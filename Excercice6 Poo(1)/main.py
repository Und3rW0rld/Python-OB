#Clases
class Vehiculo:
    color = None
    ruedas = None
    puertas = None
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def imprimirData(self):
        print("El coche tiene estas características:",
              "\nColor:", self.color,
              "\nNúmero de ruedas:", self.ruedas,
              "\nNúmero de puertas:", self.puertas,
              "\nVelocidad punta:", self.velocidad,
              "\nCilindrada:", self.cilindrada)
#Metodo main
def Main():
    carro = Coche("negro", 4, 5, 280, "973 centimetros cubicos")
    carro.imprimirData()

if __name__ == '__main__':
    Main()
