
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

x = 1
y = 2
z = 3

# if x != 0:
#     print("x is not 0")
#
# if y == 0:
#     print("y is 0")
# else:
#     print("y is not 0")
#
# if z is 0:
#     print("z is 0")
# elif z == 100:
#     print("z is not 0, but z is 100")
# else:
#     print("z is not 0 and z is not 100")

x = 101
if x < 10:
    print(f"{x} è minore di 10")
elif x == 10:
    print(f"{x} è uguale a 10")
elif x == 100:
    print(f"{x} è uguale a 100")
else:
    print(f"{x} è maggiore di 10 e diverso da 100")
print('Fine!')
