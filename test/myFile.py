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


myList = []
print(myList)
for item in range(0, 10):
    if item % 2 == 1:
        myList.append(item)
print(myList)

print([item for item in range(0, 10) if item % 2 == 1])
