
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
from os import path as p

# name = input("Name: ")
# print(f"Name is {name}")
# print(type(name))
# print(type(int(name)))

# filename = "test.txt"
# print(p.isfile(filename))
# myFileW = open(filename, "w")
# print(type(myFileW))
# myFileW.write(name + "\n")
# myFileW.close()

# with open("test1.txt", "a") as f:
#     print("Python!!!", file=f)
# f.close()

# try:
#     myFileR = open("test100.txt", "r")
#     content = myFileR.read()
#     print(f"Content: {content}")
# except Exception as e:
#     print(f"File not opened: {e}")

i = input("Inserisci il tuo indirizzo email: ")
try:
    # 1/0
    if len(i.replace(' ', '').replace('\t', '')) < 5:
        raise ValueError("Email troppo corta!!!!")
    elif ('@' not in i) or ('.' not in i):
        raise ValueError("Formato Email non valido!!!!")
    print("Valore inserito: ", i)
except (ValueError, ZeroDivisionError) as e:
    print("Errore!!! ", e)
print("The End!")
