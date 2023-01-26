import pickle
class Vehiculo:
    marca = None;
    modelo = None;
    velocidadPunta = None;

    def __init__(self, marca, modelo, velocidadPunta):
        self.marca = marca;
        self.modelo = modelo;
        self.velocidadPunta = velocidadPunta;

    def toString(self):
        print(f"El coche es un: {self.marca} {self.modelo} cuya velocidad punta es: {self.velocidadPunta} km/h");

def main():
    carro = Vehiculo("Nissan", "Nismo", 315);

    file = open("datos.bin", "wb");
    pickle.dump(carro, file);
    file.close();
    filer = open("datos.bin", "rb")
    nuevocarro = pickle.load(filer);
    filer.close();
    nuevocarro.toString();


if __name__ == '__main__':
    main();

