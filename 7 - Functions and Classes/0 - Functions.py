
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


def readMyFile(fileName: str):
    try:
        f = open(fileName, "r")
        content = f.read()
        return True, content
    except Exception as e:
        return False, e


def getUserInput():
    s = None
    while not s:
        s = input("Input: ")
    return s


fileN = getUserInput()
result, x = readMyFile(fileN)
if result:
    print(f"Content: {x}")
else:
    print(f"File not opened: {x}")
