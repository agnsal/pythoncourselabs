
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
# # print(int('string'))

# print(float(1.2))
# print(float(False))
# print(float(True))
# print(float(5))
# print(float(3.987))
# # print(float('string'))
#
# print(str('string'))
# print(str(False))
# print(str(True))
# print(str(10))
# print(str(1.5))
# print(str(1.598))
#
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


def boolMaker(inputVar):
    result = bool(inputVar)
    return result

def testDef():
    print('Def!!!')


# myBool = boolMaker(0)
# print(myBool)
# myBool = boolMaker(1)
# print(myBool)
# myBool = boolMaker(2)
# print(myBool)
# myBool = boolMaker(3)
# print(myBool)

for i in range(0, 4):
    myBool = boolMaker(i)
    print(myBool)


test = testDef()
print(type(test))

# ToDo: Check if user input is not empty.
