from functools import reduce


# def sommaAndRaddoppia(x, y):
#     return (x + y) * 2


def sommaAndRaddoppia(x, y):
    '''
    Funzione che calcola la somma di x e y e dopo la raddoppia (x + y) * 2.
    :param x: Primo addendo, è un numero (int oppure float)
    :param y: Secondo addendo, è un numero (int oppure float)
    :return: Numero (int oppure float)
    '''
    return raddoppia(x + y)


def reduceLongExample(l: list):
    '''

    :param l:
    :return:
    '''
    assert isinstance(l, list)
    if len(l) > 1:
        res = l[0]
        for i in range(1, len(l)):
            res = sommaAndRaddoppia(res, l[i])
        return res
    elif len(l) == 1:
        return l[0]
    else:
        return 0


def raddoppia(x):
    return x * 2


def dispari(x):
    return x % 2 == 1


def myMinOttimizzata(lista):
    assert isinstance(lista, list)
    c = 0
    res = lista[0]
    for i in lista[1:]:
        print("c:", c)
        c += 1
        if i < res:
            res = i
    return res


def myMin(lista):
    assert isinstance(lista, list)
    res = lista[0]
    c = 0
    for i in lista:
        print("c:", c)
        c += 1
        if i < res:
            res = i
    return res


l = [1, 2, 3, 4]

# mapResult = map(raddoppia, l)
# mapRersultList = list(mapResult)
# print(mapRersultList, type(mapResult))

# mapResult = map(lambda x: x * 2, l)
# mapRersultList = list(mapResult)
# print(mapRersultList, type(mapResult))

# d = filter(dispari, l)
# result = list(d)
# # result = [item for item in d]
# # result = []
# # for item in d:
# #     result.append(item)
# print(result, type(d))

d = filter(lambda x: x % 2 == 1, l)
result = list(d)
print(result, type(d))

# reduceResult = reduce(sommaAndRaddoppia, l)
# print(reduceResult, type(reduceResult))

# reduceResult = reduce(lambda x, y: (x + y) * 2, l)
# print(reduceResult, type(reduceResult))

# # longReduceResult = reduceLongExample([])
# longReduceResult = reduceLongExample(l)
# print(longReduceResult)

# minList = myMinOttimizzata(l)
# print(minList)
#
# minList = reduce(lambda x, y: x if x <= y else y, l)  # Commento
# print(minList)
