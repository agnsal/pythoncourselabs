lista = [1, 2, "ciao", 3, 5]
iteratore = iter(lista)

print("Lista: ", lista, type(lista))
print("Iteratore: ", iteratore, type(iteratore))

# listaDaIteratore = []
# for i in iteratore:
#     listaDaIteratore.append(i)

# listaDaIteratore = [x for x in iteratore]

listaDaIteratore = list(iteratore)
print("listaDaIteratore: ", listaDaIteratore)

printNext = lambda i: print(next(i))
while True:
    try:
        printNext(iteratore)
    except Exception as e:
        print("Stop!!! Out of range!!!")
        break
