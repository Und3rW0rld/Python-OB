def Main():

    def esBisiesto(year):
        result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return result
    year = 2016
    if(esBisiesto(year)):
        print("El año", year, "es bisiesto")
    else:
        print("El año", year, "no es bisiesto")

if __name__ == '__main__':
    Main()