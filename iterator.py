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

printNext = lambda i: next(i)
while True:
    try:
        n = printNext(iteratore)
        if n:
            print(n)
        else:
            raise StopIteration("Out of Range!!! Gli elementi dell'iter sono finiti!")
    except Exception as e:
        print("Stop!!!", e)
        break
