
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


a = 1
# at = type(a)
# aID = id(a)
#
# b = 1.0
# bt = type(b)
#
# c = "python 3"
# ct = type(c)
# d = None
# dt = type(d)
# e = False
# et = type(e)
#
# print("A:")
# print(a)
# print(at)
# print(aID)
#
# print("B:")
# print(b)
# print(bt)
#
# print("C:")
# print(c)
# print(ct)
# print("D:")
# print(d)
# print(dt)
# print("E:")
# print(e)
# print(et)

# What's the type of "1"?
# ToDo: Print Function with IDs too.


d = {
    "a": {
        "input": a,
        "type": type(a),
        "id": id(a),
        # "other": None,
        # "x": [1, [2, 3]]
    },
    "b": {}
}

# print(d)
# print(d["a"])
# print(d["a"]["id"])
# print(d["a"]["type"])
# print(d["a"]["x"][1][-1])

print(type(d))
print(type(d["a"]))
print(type(d["a"]["input"]))
print(type(d["a"]["id"]))
print(type(d["a"]["type"]))
