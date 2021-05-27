
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

'''
Questo è un commento
su più linee
'''
# Intero
a = 1  # A è una variabile
at = type(a)
aID = id(a)

# Float
b = 1.0
bt = type(b)

# Stringa
c = "python 3"
ct = type(c)

# None
d = None
dt = type(d)

# Booleano
e = False
et = type(e)

print("A:")
print(a)
print(at)
print(aID)
a = "ciao"
print("Nuovo A:")
print(a)
print(type(a))
print(id(a))
newA = a
print(id(newA))

print("B:")
print(b)
print(id(b))
print(bt)

print("C:")
print(c)
print(id(c))
print(ct)
print("D:")
print(d)
print(f"ID: {id(d)}")
print(dt)
print("E:")
print(e)
print(id(e))
print(et)

print(f"#### Domanda0: {id(e) == id(b)} ####")
print(f"#### Domanda1: {id(newA) == id(a)} ####")

# What's the type of "1"?
# ToDo: Print Function with IDs too.
