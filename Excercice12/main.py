def main():
    listaPaises = input("Ingrese una lista de paises separados por coma: ").split(",")
    listaPaises = list(map(lambda x: x.strip().capitalize(), listaPaises))
    listaPaises = set(listaPaises)
    listaPaises = sorted(list(listaPaises))
    print(", ".join(listaPaises))

if __name__ == '__main__':
    main();