
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


def summ(x, y):
    return x + y


def difference(x, y):
    return x - y


def operations(x, y, op: str):
    assert isinstance(x, int) or isinstance(x, float)
    assert isinstance(y, int) or isinstance(y, float)
    assert isinstance(op, str)
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    else:
        return f"Not allowed op: {op}"



# print(summ(1, 4))
# print(summ(7, -2))
# print(difference(7, 2))
# print(difference(2, 7))

print(operations(2, 3, "+"))
print(operations(2, 3, "-"))
print(operations(2, 3, "*"))
print(operations(2, 3, "ciao"))
print(operations(4.8, 3, "+"))

try:
    print(operations("ciao", 3, "+"))
except Exception as e:
    print("Inputs are not valid!!!")
