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


def dictExplorer(d: dict):
    for k in d:
        if isinstance(d[k], dict):
            print(f'Dict!!! {k}: {d[k]}')
            dictExplorer(d[k])
        else:
            print("NOT a Dict!!!")
            print(f"{k}: {d[k]}")


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

myDict = {
    'a': 1,
    'b': 2,
    'c': {
        'd': {
            'e': 3,
            'f': [4, 5]
        }
    },
    'g': 'ciao'
}

dictExplorer(myDict)


