import time as t
def Main():
    horas = t.localtime().tm_hour
    minutos = t.localtime().tm_min
    tiempo = t.localtime().tm_sec
    horas = horas*60*60
    minutos = minutos*60
    tiempo += horas+minutos
    if tiempo > 68400:
        print("Es hora de salir!")
    else:
        tiempo = 68400 -  tiempo
        horas = tiempo//3600
        tiempo = tiempo - (horas*3600)
        minutos = tiempo // 60
        tiempo = tiempo - (minutos * 60)
        print(f"Faltan {horas} horas, {minutos}, minutos y {tiempo} segundos para la salida")

if __name__ == '__main__':
    Main()