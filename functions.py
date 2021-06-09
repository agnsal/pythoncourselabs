def simpleFunction():
    print("Simple function!")


def simpleSum(x, y):
    return x + y


def myFunction(a, b, c):
    print(a)
    print(b)
    print(c)
    print("Fine!!!")
    return None

mfResult = myFunction(1, 2, 3)
print("La funzione è stata eseguita con successo!")
print(f"Result: {mfResult}, Type: {type(mfResult)}")
sResult = simpleFunction()
print("La funzione è stata eseguita con successo!")
print(f"Result: {sResult}, Type: {type(sResult)}")
result = simpleSum(1, 2)
print(f"Result: {result}, Type: {type(result)}")
