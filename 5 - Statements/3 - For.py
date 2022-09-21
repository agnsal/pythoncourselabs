
'''
Copyright 2021-2022 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

# l = [0, 1, 2, 3, 4, 5]
# for x in l:
#     print(x)
# print("The end")

# d = {'ita': 'ciao', 'eng': 'hello'}
# for y in d:
#     print(d[y])
# print('The End')
#
# s = 'python'
# for z in s:
#     print(z)
# print('The End')
#
# for a in range(0, 4):
#     print(f"a: {a}")
# print('The End')
#
# for b in range(0, 10, 3):
#     print(f"b: {b}")
# print('The End')
#
# myList = [n for n in range(0, 10) if n % 2 == 0]
# print(f"myList: {myList}")


# risultato = {}
#
# myDict = {'nome': 'agnese', 'cognome': 'salutari', 'indirizzo': 'via X'}
# for item in myDict:
# # for item in myDict.keys():
#     print(f"Key: {item}")
# for item in myDict.values():
#     print(f"Value: {item}")
# for item in myDict.items():
#     print(item)
#     print(type(item))
# for k, v in myDict.items():
#     print(f"Key: {k} - Value: {v}")
#     risultato[f"myApp_{k}"] = v.upper()

# myList = ['cognome', 'nome']
# for k in myList:
#     risultato[k] = myDict[k]
#
# print(f"Risultato: {risultato}")


# for z in range(3, 10, 2):
#     print(z)


l = []
for x in range(1, 101):
    if x % 2 == 0:
        l.append(x)
print(f"Verboso: {l}")

l = [x for x in range(1, 101) if x % 2 == 0]
print(f"Breve: {l}")

