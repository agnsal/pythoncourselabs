
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

print('1) ----')
x = 1
y = x
z = 2
print(y is x)
print(y is not z)
print('-------')

print('2) ----')
x = 1
y = 1
z = 2
print(y is x)
print(y is not z)
print('-------')

print('3) ----')
x = 1000
y = 1000
print(y is x)
print(id(x) == id(y), id(x), id(y))
y += 0
print(y is x)
print(id(x) == id(y), id(x), id(y))
print('-------')

