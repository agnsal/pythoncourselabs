
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

# print(int(10))
# print(int(False))
# print(int(True))
# print(int(2.1))
# print(int(2.999))
# # print(int('string'))  # Errore!!!
# print(int('100'))
# # print(int('100.2'))  # Errore!!!

# print(float(1.2))
# print(float(False))
# print(float(True))
# print(float(5))
# print(float(3.987))
# # print(float('string'))  # Errore!!!
# print(float('4.3'))
# print(float('4'))

# print(str('string'))
# print(str(False))
# print(str(True))
# print(str(10))
# print(str(1.5))
# print(str(1.598))

# print(bool(False))
# print(bool(True))
# print(bool('string'))
# print(bool(''))
# print(bool(100))
# print(bool(0))
# print(bool(0.12))
# print(bool([1, 2]))
# print(bool([]))
# print(bool({'a': 10}))
# print(bool({}))

# ToDo: Check if user input is not empty [x = input('...')]

# x = input("Scrivi: ")
# if bool(x.replace(' ', '').replace('\t', '')):
#     print('PIENO')
# else:
#     print('VUOTO')

# x = input("Scrivi qualcosa: ")
# if x.replace(' ', '').replace('\t', ''):
#     print("Hai scritto: ", x)
# else:
#     print("Non hai scritto niente")

if not input("Inserisci una stringa: ").replace(' ', '').replace('\t', ''):
    print('input non valido')
else:
    print('Input valido')

# v = input("Inserisci una stringa: ")
# lv = len(v.replace(' ', '').replace('\t', ''))
# print('lv: ', lv)
# if lv == 0:
#     print('input non valido')
# else:
#     print('Input valido')


