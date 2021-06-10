def testF():
    print("Funzione Test!!!")


def testF2(x):
    print("Funzione Test", x)


class Veicolo:
    counter = 0

    def __init__(self, targa):
        self.__targa = targa
        Veicolo.counter += 1

    def printTarga(self):
        print("Targa:", self.__targa)


class Automobile(Veicolo):
    categoria = "automobile"

    def __init__(self, targa, sottocategoria):
        super().__init__(targa)
        self.__sottocategoria = sottocategoria

    def printSottocategoria(self):
        print(self.__sottocategoria)
