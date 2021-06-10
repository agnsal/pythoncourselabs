# import functools
from functools import reduce

def simpleFunction():
    print("Simple function!")


def simpleSum(x, y):
    z = x + y
    return z


def simpleProdGetter():
    def simpleProd(x, y):
        return x * y
    return simpleProd


def functionCaller(fToCall, a, b):
    return fToCall(a, b)


def myFunction(a, b, c=0):
    print(a)
    print(b)
    print(c)
    print("Fine!!!")
    return None


def protectedFunction(x: str):
    assert isinstance(x, str)
    print("Assert OK!")
    print("Stringa: " + x)


def argsFunction(x, *args):
    print("x: ", x)
    print(args, type(args))


def kwargsFunction(**kwargs):
    print(kwargs, type(kwargs))


def workOnX(x):
    x += 1
    print(x)


def workOnDict(d):
    d["test"] = "ciao"
    print("D: ", d)


def workOnList(l):
    l.append("ciao")
    print("L: ", l)


def nonRicorsiva(l):
    for elem in l:
        print(elem)


def ricorsiva(l):
    for elem in l:
        if isinstance(elem, list):
            ricorsiva(elem)
        else:
            print(elem)


# mfResult = myFunction(1, 2, 3)
# print("La funzione è stata eseguita con successo!")
# # print(f"Result: {mfResult}, Type: {type(mfResult)}")
# # sResult = simpleFunction()
# # print("La funzione è stata eseguita con successo!")
# # print(f"Result: {sResult}, Type: {type(sResult)}")
# # result = simpleSum(1, 2)
# # print(f"Result: {result}, Type: {type(result)}")
# mfResult = myFunction(b=1, c=2, a=3)
# print("La funzione è stata eseguita con successo!")
# mfResult = myFunction(2, b=1)
# print("La funzione è stata eseguita con successo!")

# protectedFunction("ciao")
# protectedFunction(10)  # Assertion Error

# argsFunction(2, "python", 100, [3, 7])
# kwargsFunction(s="python", x=0, y=1)
# r = simpleSum(1, 2)
# print(r)


# y = 4
# workOnX(y)
# print(y)


# myDict = {"x": 1}
# # workOnDict(myDict)
# # print("myDict: ", myDict)
# workOnDict(myDict.copy())
# print("myDict: ", myDict)

# myList = [0, 1]
# workOnList(myList)
# print("myList: ", myList)

# myDict = {"x": 1}
# workOnX(myDict['x'])
# print(myDict)

# v = simpleProdGetter()
# print("V:", v, type(v))
# simpleProdRes = v(1, 2)
# print("simpleProdRes:", simpleProdRes, type(simpleProdRes))
#
# functionCallerResult = functionCaller(simpleSum, 2, 3)
# print("functionCallerResult:", functionCallerResult, type(functionCallerResult))

# lambdaRef = lambda s: print(s)
# lambdaRef("ciao")

if __name__ == "__main__":
    l = [0, 1, 2, ["ciao", "python", 3], 4, 5, [6, 7]]
    print("Non ricorsiva:")
    nonRicorsiva(l)
    print("Ricorsiva:")
    ricorsiva(l)
