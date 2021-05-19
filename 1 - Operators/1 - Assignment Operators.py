
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

# print("=")
x = 4
# print(x)
# print("+=")
# x += 1  # x = x + 1
# print(x)
# print("-=")
# x -= 1  # x = x - 1
# print(x)
# print("*=")
# x *= 2
# print(x)
# print("/=")
# x /= 2
# print(x)
# print("//=")
# x //= 3
# print(x)
# print("%=")
# x %= 3
# print("**=")
# x **= 2
# print(x)

# ToDo: Use assign operators in 1.0 ToDo.


def operations(x, y, op: str):
    assert isinstance(x, int) or isinstance(x, float)
    assert isinstance(y, int) or isinstance(y, float)
    assert isinstance(op, str)
    if op == "+":
        x += y
        return x
    elif op == "-":
        x -= y
        return x
    elif op == "*":
        x *= y
        return x
    else:
        return f"Not allowed op: {op}"


print(operations(2, 2, '*'))
