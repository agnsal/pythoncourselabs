
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

# x = int(input("x = "))
#
# print(x > 0)
# print(x < 0)
# print(x == 0)
# print(x != 0)
# print(x >= 0)
# print(x <= 0)

# ToDo: Use if statements to make more detailed prints.

# x = int(input("x = "))
# if x < 0:
#     print(x < 0)
#     print('negativo', x)
# elif x == 0:
#     print(x == 0)
#     print('UGUALE')
# elif x < 50:
#     print(x < 50)
#     print('minore di 50 ', x)
# elif x <= 100:
#     print(x < 100)
#     print(x == 100)
#     print('compreso tra 50 e 100 ', x)
# else:
#     print('> 100')
# print('Fine statement')

# valoriAmmessi = ["si", "no"]
# while True:
#     x = int(input("x = "))
#     if x > 0:
#         print("Hai inserito", x, "che è maggiore di 0")
#     elif x < 0:
#         print("Hai inserito", x, "che è minore di 0")
#     else:
#         print("Hai inserito", x, "che è uguale a 0")
#     c = input("Vuoi continuare? si/no: ")
#     while c not in valoriAmmessi:
#         c = input("Vuoi continuare? si/no: ")
#     if c == "no":
#         break

# x = int(input("x = "))
# if x > 0:
#     print('> 0')
# elif x < 0:
#     print('< 0')
# else:
#     print('= 0')
# print('Fine statement')

# ToDo: Check if x in in one of the following intervals: [-2, 5], (10, 100], (200, 300)

x = input("Inserisci un numero: ")
try:
    x = float(x)
    if (-2 <= x <= 5) or (10 < x <= 100) or (200 < x < 300):
        print(f"{x} è contenuto in uno degli intervalli")
    else:
        print(f"{x} NON è contenuto in alcuno degli intervalli")
except:
    print("Il valore inserito non è corretto!!!")
    print(x.upper())
    print(isinstance(x, str))

# x = 10
# y = "ciao"
# assert isinstance(x, int) and isinstance(y, float)
