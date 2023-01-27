from functools import reduce
def main():
    def esimpar(num):
        if num % 2 == 0:
            return False;
        else:
            return True;
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
    impares = list(filter(esimpar, numeros))
    print(reduce(lambda x, y: x+y, list(impares)))

if __name__ == '__main__':
    main()