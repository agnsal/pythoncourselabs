#from test.Utils import printStr

class Test:
    __myVar = None
    pub = 1

    def __init__(self, x):
        self.setMyVal(x)
        pass

    def setMyVal(self, x):
        self.__myVar = str(x)
        # printStr(self.__myVar)

    def getMyVal(self):
        return self.__myVar


# verificaIta = Test("Titolo: ita")
# verificaMat = Test("Titolo: mat")
# print(verificaIta.getMyVal())
# print(verificaMat.getMyVal())
# # t.pub = 10
# # myVal = t.getMyVal()
# # print(type(t))

class Veicolo:
    __className = "Veicolo"

    def __init__(self, targa):
        self.__targa = targa

    def changeTarga(self, newTarga):
        self.__targa = str(newTarga)

    def getTarga(self):
        return f"Targa: {self.__targa}"


class Automobile(Veicolo, Test):
    __className = "Automobile"

    def __init__(self, targa, marca):
        self.__marca = marca
        super().__init__(targa)

    def getMarca(self):
        return self.__marca

    def getClassName(self):
        return self.__className


# v = Veicolo("123")
# print(v.getTarga())
# v.changeTarga(456)
# print(v.getTarga())
a = Automobile("789", "x")
# print(a.getTarga())
# print(a.getMarca())

# print(v.__className)
# print(a.__className)
#
# a.__className = "hackedClassName"
# print(a.getClassName())

print(a.getMyVal())
