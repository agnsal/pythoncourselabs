from test.Utils import printStr

class Test:
    __myVar = None

    def __init__(self, x):
        self.setMyVal(x)
        pass

    def setMyVal(self, x):
        self.__myVar = x
        printStr(self.__myVar)

    def getMyVal(self):
        return self.__myVar
