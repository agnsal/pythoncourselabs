from functools import reduce


# print("Ciao!")
# x = 10
# y = 4
# print("Inizio!")
# if x == 10:
#     print("x è uguale a 10")
#     print("test 1")
#     if y % 2 == 0:
#         print("y è pari")
#         print("test 2")
# print("Fine!")

#

# l = [1, 2, 3,
#      4, 5]
# print(l)

# z = 1
# if z > 2:
#     print("test 1")
# elif z == 10:
#     print("test 2")
# else:
#     print("test 3")

# q = 10
# while q < 30:
#     print(q)
#     q += 10
# print("No! ", q)
# print("Fine!")

# l = ["paola", "andrea", "felice"]
# print(l)
# stop = len(l)
# print(stop)
# i = 0
# while i < stop:
#     print(l[i])
#     i += 1
# print(i)

# while True:
#     i = input("Inserisci qualcosa:\n")
#     print(i, ' - ', bool(i))
#     if not i:  # bool(i) is False
#         break
#     if i == "ciao":
#         continue
#     print("test")
# print("Fine!")

# n = 10
# while n >= 0:
#     print(n)
#     n -= 1
#     if n == 5:
#         break
# else:
#     print("Fine While")
# print("Fine!")

# n = 10
# while n >= 0:
#     n -= 1
#     if n == 5:
#         continue
#     print(n)
# else:
#     print("Fine While")
# print("Fine!")


# l = ["ciao", "hello", "hi"]
# l = "Ciao Python!"
# print(l[0])
# for item in l:
#     print(item)

# d = {"nome": "agnese", "cognome": "salutari"}
# for k in d:
#     print(k, ' - ', d[k])
# dv = d.values()
# print(dv, ' - ', type(dv))
# for v in d.values():
#     print(v)
# for i in d.items():
#     print(i, ' - ', type(i))
# for k in d.keys():
#     print(k)


# myList = []
# print(myList)
# for item in range(0, 10, 2):
#     myList.append(item)
# print(myList)
#
# print([x for x in range(0, 3)])
# print([item for item in range(0, 1001)])


# myList = []
# print(myList)
# for item in range(0, 10):
#     if item % 2 == 1:
#         myList.append(item)
# print(myList)

# print([item for item in range(0, 10) if item % 2 == 1])
#
# print([item * 2 if item % 2 == 1 else item for item in range(0, 10)])

# print(ord('a'), ' - ', ord('b'))

# parola = "hello"
# d = {}
# for lettera in parola:
#     d[lettera] = ord(lettera)
# print(d)

# d = {k: ord(k) for k in parola}
# print(d, ' - ', type(d))


# parola = "doppione"
# myList = []
# for lettera in parola:
#     myList.append(lettera)
# print(myList)

# mySet = set()
# for lettera in parola:
#     mySet.add(lettera)
# print(mySet)
#
# print({lettera for lettera in parola})

# myList = ["franco", "martina", "carla"]
# # for x in myList:
# #     print(x)
# for posizione, x in enumerate(myList):
#     print('Pos: ', posizione, ' - Elem: ', x)
#     print(x, ' è amico di ', myList[posizione - 1])


# s = "Ciao Python!!!"
# delta = 2
# # Cifro
# c = ''
# for lettera in s:
#     o = ord(lettera)
#     print(lettera, ' - ', o, ' - ', chr(o))
#     newOrd = o - delta
#     c += chr(newOrd)
# print(c)
#
# # Decifro
# d = 0
# while True:
#     t = ''
#     for lettera in c:
#         o = ord(lettera)
#         newOrd = o + d
#         t += chr(newOrd)  # t += chr(o + d) oppure t += chr(ord(lettera + d))
#     print(d, ': ', t)
#     if not input("Procedo? ").strip():
#         break
#     else:
#         d += 1
# print(t)


def laMiaFunzione():
    print("Ciao Python!")
#
#
# def laMiaFunzioneConParam(myStr):
#     print(f"Il parametro è: {myStr}")
#     print("Fine funzione!")
#
#
# def laMiaFunzioneConParams(a="sono a", b="sono b", c="sono c"):
#     print(f"I parametri sono: '{a}', '{b}' e \"{c}\"")
#     print("Fine funzione!")
#
#
# print("Prima della funzione")
# laMiaFunzioneConParams(c="sono la nuova c!", b="sono il sostituto di b", a="sono la nuova a")
#
# print("Dopo la funzione")

# def argsFunction(x, y, *args):
#     print(args)
#     print(type(args))
#     s = 0
#     for a in args:
#         print(f"{a} è uno degli args")
#         s += a
#     print(f"La somma degli args è: {s}")
#     print(x, ' - ', y)


# def kwargsFunction(x, **kwargs):
#     print(f"x: {x}")
#     print(kwargs)
#     print(type(kwargs))
#     for i in kwargs.items():
#         print(i)
#     laMiaFunzione()
#     myRis = (100, 1)
#     return myRis
#
#
# x, y = kwargsFunction("sono x", b=2, a=1, z=3, c=20)
# print(x, ' - ', y)


# x = 100
# print(f"Inizio - x = {x}")
#
# def raddoppia(myInt):
#     x = myInt * 2
#     print(f"Raddoppia - x = {x}")
#     return x
#
# risultato = raddoppia(x)
# print(f"Risultato: {risultato}")
# print(f"Fine - x = {x}")
# x = risultato
# x = raddoppia(20)
# print(f"Fine 2 - x = {x}")


# def raddoppiaLista(l):
#     r = []
#     for elem in l:
#         r.append(elem * 2)
#     return r

# myList = [1, 2, 3]
# risultato = raddoppiaLista(myList)
# print(f"Risultato: {risultato}")
# print(f"MyList: {myList}")

# def somma(x):
#     x += 1000
#     # print(x)
#     return x
#
# def raddoppiaDizionario(d):
#     for k in d:
#         d[k] = 2 * d[k]
#     return d
#
# myVar = 10
# print(f"Inizio - myVar: {myVar}")
# risultato = somma(myVar)
# print(risultato)
# print(f"Fine - myVar: {myVar}")
#
# print("########")
# myDiz = {"primo": 1, "secondo": 2, "terzo": 3}
# print(f"Inizio - myDiz: {myDiz}")
# risultato1 = raddoppiaDizionario(myDiz.copy())
# print(risultato1)
# print(f"Fine - MyDiz: {myDiz}")
# print(myDiz is risultato1)  # id(myDiz) == id(risultato1)

# def myFun():
#     print("Funzione eseguita!")
#
# mf = myFun
# print(mf, ' - ', type(mf))
# myFun()
# mf()


# def somma(a, b):
#     return a + b
#
# print(somma(10, 20))
#
# s = lambda a, b: a + b
# print(s(10, 20))


#
# def test():
#     x = "ciao"
#     y = "Python"
#     print('Funzione: ', x, ' - ', y)
#     print('Funzione: ', id(x), ' - ', id(y))
#     risultato = x + y
#     return risultato
#
# def nuovoTest():
#     x = "ciao"
#     y = "Python"
#     print('Funzione: ', x, ' - ', y)
#     print('Funzione: ', id(x), ' - ', id(y))
#     risultato = x + y
#     return risultato
#
#
# x = 10
# y = 100
# print('Dichiarazione: ', x, ' - ', y)
# print('Dichiarazione: ', id(x), ' - ', id(y))
# test()
# print('Dopo la funzione: ', x, ' - ', y)
# print('Dopo la funzione: ', id(x), ' - ', id(y))
# output = test()
# print(output)

# def getMin(a, b):
#     res = a
#     if a > b:
#         res = b
#     return res

# l = [10, 100, 4, 1000]
#
# minNum = l[0]
# for item in l[1:]:
#     minNum = min(minNum, item)
# print(minNum)
#
# print(reduce(lambda a, b: min(a, b), l))

print(reduce(lambda a, b: min(a, b), [10, 100, 4, 1000]))
