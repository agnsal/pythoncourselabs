
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

# x = "stringaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n" \
#     "stringa"
# print(x)
#
# print('z' in 'python')
# print('tho' in 'python')

# a = 1  # Questa è una variabile
# at = type(a)
# aID = id(a)
# b = 1.0
# bt = type(b)
# c = "python 3"
# ct = type(c)
# d = None
# dt = type(d)
# e = False
# et = type(e)

# print("A:")
# print(a)
# print(at)
# print(aID)
# print("B:")
# print(b)
# print(bt)
# print("C:")
# print(c)
# print(ct)
# print("D:")
# print(d)
# print(dt)
# print("E:")
# print(e)
# print(et)

x = "My GLOBAL X"

def studyVar(var):
    # print(f'The variable is: \' {var}')
    # print(f"The variable type is: {type(var)}")
    # print(f"The variable id is: {id(var)}")
    #print(f"------------ x: {x}")
    y = "STUDYVAR VARIABLE"
    #print(f"LOCAL!!!!! {y}")
    # print(f"X1: {x}")
    x = "ciao"
    def test():
        nonlocal x
        x = "python!!!!!"
        print(f"ENCLOSED!!!!! {x}")
        return y

    res = test()
    print(f"NON LOCAL: {x}")
    #print(f"Y: {res}")


studyVar(1)
print(f"GLOBAL!!!!!!! {x}")

# studyVar(1.7)
# studyVar(True)
# studyVar("ciao")
# l0 = [8, 9]
# l1 = [1, 2]
# studyVar(l0)
# studyVar(l1)

# What's the type of "1"?
# ToDo: Print Function with IDs too.
