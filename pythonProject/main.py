def main():
    file = open("artchivo.txt", "a")
    file.write("Esto es un texto nuevo para nuestro archivo\n")
    file.close()
if __name__ == '__main__':
    main()