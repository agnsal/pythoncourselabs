
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
# from os import path
# print(path.exists("../4 - Lists and Dicts/0 - Lists Methods.py"))

# name = input("Name: ")
# print(f"Name is {name}")
#
# myFileW = open("test4.txt", "w")
# myFileW.write(name + "\n" + name + "\n" + name + "\n" + name)
# myFileW.close()
# myFileW = open("test3.txt", "r")
# print(myFileW.read().split('\n'))
# myFileW.close()
#
# with open("test3.txt", "w") as t3:
#     print(t3.read().split('\n'))
#
# try:
#     myFileR = open("test.txt", "r")
#     content = myFileR.read()
#     print(f"Content: {content}")
# except Exception as e:
#     print(f"File not opened: {e}")
#
# print("Hey!!!!!")

import os


def copyFile(file1:str, file2:str):
    try:
        if not os.path.exists(file1):
            raise FileNotFoundError("File1 non presente")

        f1 = open(file1, "r")
        f2 = open(file2, "w")
        line = f1.readline()
        while line != '':  # The EOF char is an empty string
            f2.write(line)
            line = f1.readline()
    except Exception as e:
        print(f"Errore!!! {e}")


copyFile("test.txt", "test2.txt")

