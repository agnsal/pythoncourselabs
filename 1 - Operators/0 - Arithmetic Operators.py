
'''
Copyright 2021 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

# x = 4
#
# print("x =", x)
# print("+")
# print(" x + 1 =", x + 1)
# print("-")
# print(" x - 5.7 =", x - 5.7)
# print("*")
# print(" x * 3 =", x * 3)
# print("/")
# print(" x / 3 =", x / 3)
# print("//")
# print(" x // 3 =", 4 // 3)
# print("%")
# print(" x % 3 =", 4 % 3)
# print("**")
# print(" x ** 2 =", x ** 2)
# print("-x")
# print(" -x =", -x)

# ToDo: Create a functions to perform these operations on inputs.


def somma(a, b):
    return a + b


def differenza(a, b):
    return a - b


def moltiplicazione(a, b):
    return a * b


# def operation(a, b, op):
#     x = None
#     if op == "+":
#         x = a + b
#     elif op == "-":
#         x = a - b
#     elif op == "*":
#         x = a * b
#     elif op == "/":
#         x = a / b
#     else:
#         print("oparatore non valido")
#     print(x)
#
#
# x = int(input("scrivi il 1 nunero"))
# y = int(input("scrivi il 2 nunero"))
# z = input("Scrivi un operatore")
# operation(x, y, z)


def operation(a, b, op):
    if op == "addizione":
        return a + b
    elif op == "sottrazione":
        return differenza(a, b)
    elif op == "prodotto":
        return moltiplicazione(a, b)
    else:
        print("Operazione non consentita!!!")


# print(somma(1, 2))
# print(operation(1, 2, "addizione"))
# print(operation(2, 3, "prodotto"))
# print(operation(2, 3, "ciao"))


operationMapping = {
    "addizione": somma,
    "sottrazione": differenza,
    "prodotto": moltiplicazione
}

funzioneDaEseguire = operationMapping['addizione']
print(funzioneDaEseguire, type(funzioneDaEseguire))
print(funzioneDaEseguire(2, 3))
