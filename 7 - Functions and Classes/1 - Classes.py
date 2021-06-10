
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


class fileReader:
    instanceCounter = 0

    def __init__(self, fileName: str="t.txt"):
        try:
            assert isinstance(fileName, str)
            self.__fileName = fileName
            self.__f = open(self.__fileName, 'r')
            fileReader.instanceCounter += 1
        except Exception as e:
            print(f"!!!!! File not opened: {e}")

    def getFileName(self):
        return self.__fileName

    def readFile(self):
        content = self.__f.read()
        return content


fm = fileReader('text.txt')
fmIs2 = fileReader('text.txt')
print(fm.readFile())
# print(fm.__fileName)  # Errore!!!
print(fm.getFileName())
print(fileReader.instanceCounter)
print(fm.instanceCounter)
fm.instanceCounter = 10
print(fm.instanceCounter)
print(fmIs2.instanceCounter)
fileReader.instanceCounter = 1000
fmIs3 = fileReader('text.txt')
print(fmIs2.instanceCounter)
