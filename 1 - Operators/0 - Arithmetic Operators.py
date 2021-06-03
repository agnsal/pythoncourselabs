
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
def op0(x, y, o):
    if o == "+":
        return x + y
    elif o == "-":
        return x - y
    elif o == "*":
        return x * y
    else:
        print('Not allowed operation!!!')
        return None


def sum(x, y):
    return x + y


def dif(x, y):
    return x - y


def prod(x, y):
    return x * y


def op1(x, y, o):
    if o == "+":
        return sum(y, y)
    elif o == "-":
        return dif(x, y)
    elif o == "*":
        return prod(x, y)
    else:
        print('Not allowed operation!!!')
        return None


opMapping = {
    "+": sum,
    "-": dif,
    "*": prod
}

# res0 = op0(1, 2, "+")
# print(res0)
# res1 = op1(1, 2, "-")
# print(res1)
print(opMapping.keys())
print(opMapping.values())
res2 = opMapping["*"](2, 3)
print(res2)
