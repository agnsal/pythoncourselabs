
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
    iNumber = 0
    name = "File Reader"

    def __init__(self, fileName: str="t.txt"):
        self.x = "ciao"
        assert isinstance(fileName, str)
        self.__fileName = fileName
        print("__fileName: ", self.__fileName)
        try:
            self.__f = open(self.__fileName, 'r')
            fileReader.iNumber += 1
        except Exception as e:
            print(f"!!!!! File not opened: {e}")

    def getFileName(self):
        return "The filename is: " + self.__fileName

    def readFile(self):
        content = self.__f.read()
        return content

    def __readFile(self):
        content = self.__f.read()
        return content

    @classmethod
    def printINumber(cls):
        print(cls.iNumber)

    @staticmethod
    def getINumber():
        return fileReader.iNumber


class fileReaderFiglio(fileReader):
    def __init__(self, filename):
        super().__init__("Figlio!!!!" + filename)

    def prova(self):
        print("Prova!!!")


# fm = fileReader('text.txt')
# print(fm.__fileName)
# print(fm.getFileName())
# print(fm.x)
# fm.x = "Hello"
# print(fm.x)
# print(fm.readFile())
# print(fm.__readFile())
# print(fileReader.iNumber)
# print(fileReader.x)
# print(fm.iNumber)
# print(fm.x)
# fm1 = fileReader('text.txt')
# print(fm1.x)
# print(fm1.iNumber)
# print(fm.iNumber)
# fm2 = fileReader('text.txt')
# fileReader.iNumber = 100
# print(fm.iNumber)
# print(fm1.iNumber)
# print(fm2.iNumber)
# fileReader.printINumber()
# print(fileReader.getINumber())
figlio = fileReaderFiglio('text.txt')
print(figlio.getFileName())
figlio.prova()
