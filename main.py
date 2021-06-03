# from collections import OrderedDict

# import logging as l
# from testPackage import *
# # from testPackage import pVar0, pVar1, pVar2
#
# l.warning("Attenzione!")
# print(pVar0)
# print(pVar1)
# print(pVar2)


def myFPrintPython():
    print("Python!!!!!")


def checker(x, k):
    if x < k:
        r = f'{x} < {k}'
    elif x == k:
        r = f'{x} == {k}'
    else:
        r = f'{x} > {k}'
    # print(r)
    myFPrintPython()
    return r


def checkerNested(myVar):
    print(f'MyVar: {myVar}')

    def innerChecker(x, k):
        if x < k:
            r = f'{x} < {k}'
        elif x == k:
            r = f'{x} == {k}'
        else:
            r = f'{x} > {k}'
        # print(r)
        return r
    return innerChecker


test = "Python"  # Global
def checkerNestedLEGB():
    test = "Ciao"  # Enclosed
    def innerChecker():
        global test
        # test = "Course"  # Local
        icVar = "icVar"
        print("Inside innerChecker: ", test, " - id: ", id(test))
        print(icVar)
    print("Inside checkerNestedLEGB: ", test, " - id: ", id(test))
    return innerChecker


def outer():
    y = 100
    print("Outer Level (Before inner call): ", y, " - id: ", id(y))
    def inner():
        nonlocal y
        y = 50
        print("Inner Level: ", y, " - id: ", id(y))
    inner()
    print("Outer Level: ", y, " - id: ", id(y))


def dictExplorer(d: dict):
    print(vsTest)
    for k in d:
        if isinstance(d[k], dict):
            print(f'Dict!!! {k}: {d[k]}')
            dictExplorer(d[k])
        else:
            print("NOT a Dict!!!")
            print(f"{k}: {d[k]}")


vsTest = 100
def sTest():
    # vsTest = 2  # It overrides global vsTest
    print(vsTest)

# a = 10
# cRes = checker(k=100, x=a)
# print(f"cRes: {cRes}")
#
# res = checkerNested("Ciao Checker!!!")
# print(f"Res: {res}, type: {type(res)}")
# # ...
# a = 10
# c = res(a, 20)
# print(f"c: {c}, type: {type(c)}")

# myDict = {
#     'a': 1,
#     'b': 2,
#     'c': {
#         'd': {
#             'e': 3,
#             'f': [4, 5]
#         }
#     },
#     'g': 'ciao'
# }
#
# dictExplorer(myDict)

# print(vsTest)
# sTest()

# resLEGB = checkerNestedLEGB()()
# print("Inside main program: ", test, " - id: ", id(test))

# outer()

l = ["agnese", "francesca"]
print(l)
l.insert(0, "paolo")
print(l)
l.pop()
print(l)
l.pop()
print(l)
