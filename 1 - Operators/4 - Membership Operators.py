
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

# print('p' in 'python')
# print('a' in 'python')
# print('py' in 'python')
# print('pn' not in 'python')

# print("a" in "python" or "n" in "python")
# print("p" in "python" and "n" in "python")


def checkString0(s: str, l: list):
    result = {}
    for lettera in l:
        if lettera in s:
            result[lettera] = True
            print(f'lettera: {lettera} is in list')
        else:
            result[lettera] = False
            print(f'lettera: {lettera} is NOT in list')
    return result


def checkString0Ottimizzato(s: str, l: list):
    result = {}
    for lettera in l:
        result[lettera] = lettera in s
    return result


# lista = input("Inserisci un testo: ").replace(' ', '').split(',')
# risultato = checkString0Ottimizzato("python", lista)
# print(risultato)

# lista = input("Inserisci un testo: ").replace(' ', '').split(',')
# stringa = "python"
# risultato = list(filter(lambda x: x in stringa, lista))
# print(risultato)


def checkString1(s: str, l: list):
    res = True
    for lettera in l:
        res = res and (lettera in s)
        if not res:
            break
    return res


def checkString1Ottimizzata(s: str, l: list):
    for lettera in l:
        if lettera not in s:
            return False
    return True


stringa = "PythonLanguage"
lista = ["y", "z", "a", "g", "L"]
print(checkString1(stringa, lista))

# stringa = "PythonLanguage"
# lista = ["y", "z", "a", "g", "L"]
# print(checkString1Ottimizzata(stringa, lista))
