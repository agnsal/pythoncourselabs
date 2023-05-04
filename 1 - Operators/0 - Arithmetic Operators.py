
'''
Copyright 2021-2023 Agnese Salutari.
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


def calcolo(x):
    print("x =", x)
    print("+")
    print(" x + 1 =", x + 1)
    print("-")
    print(" x - 5.7 =", x - 5.7)
    print("*")
    print(" x * 3 =", x * 3)
    print("/")
    print(" x / 3 =", x / 3)
    print("//")
    print(" x // 3 =", 4 // 3)
    print("%")
    print(" x % 3 =", 4 % 3)
    print("**")
    print(" x ** 2 =", x ** 2)
    print("-x")
    print(" -x =", -x)


check = [str(c) for c in range(1, 101)]
numero = ''
while numero not in check:
    numero = input("Inserisci un numero tra 1 e 100:\n")
calcolo(int(numero))
