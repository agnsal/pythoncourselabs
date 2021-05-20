
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

text = """Fratelli d'Italia,
L'Italia s'è desta;
Dell'elmo di Scipio
S'è cinta la testa.
Dov'è la Vittoria?
Le porga la chioma;
Ché schiava di Roma
Iddio la creò.

Stringiamci a coorte!
Siam pronti alla morte;
L'Italia chiamò.

Noi siamo da secoli
Calpesti, derisi,
Perché non siam popolo,
Perché siam divisi.
Raccolgaci un'unica
Bandiera, una speme;
Di fonderci insieme
Già l'ora suonò.

Stringiamci a coorte!
Siam pronti alla morte;
L'Italia chiamò.

Uniamoci, amiamoci;
L'unione e l'amore
Rivelano ai popoli
Le vie del Signore.
Giuriamo far libero
Il suolo natio:
Uniti, per Dio,
Chi vincer ci può?

Stringiamci a coorte!
Siam pronti alla morte;
L'Italia chiamò.

Dall'Alpe a Sicilia,
Dovunque è Legnano;
Ogn'uom di Ferruccio
Ha il core e la mano;
I bimbi d'Italia
Si chiaman Balilla;
Il suon d'ogni squilla
I Vespri suonò.

Stringiamci a coorte!
Siam pronti alla morte;
L'Italia chiamò.

Son giunchi che piegano
Le spade vendute;
Già l'Aquila d'Austria
Le penne ha perdute.
Il sangue d'Italia
E il sangue Polacco
Bevé col Cosacco,
Ma il cor le bruciò.

Stringiamci a coorte!
Siam pronti alla morte;
L'Italia chiamò."""

# print(f"####### Firts 100 text chars #######\n{text[0:100]}")
# textSplit = text.split('\n')
# print(f"####### textSplit type #######\n{type(textSplit)}")
# print(f"####### 1st textSplit line#######\n{textSplit[0]}")
# print(len(textSplit))
# textAdd = "!!! Inno d'Italia !!!\n" + text + "\n^^^^^^^^^^^^^^^^^^^^^^^^^^^"
# print(f"######## First 100 textAdd chars########\n{textAdd[0:100]}")
# print(f"######## Last 100 textAdd chars########\n{textAdd[-100:-1]}")
# textJoin = "-".join(text)
# print(f"######## First 100 textJoin chars########\n{textJoin[0:100]}")
# textUpper = text.upper()
# print(f"######## First 100 textUpper chars########\n{textUpper[0:100]}")
# textLower = text.lower()
# print(f"######## First 100 textLower chars########\n{textLower[0:100]}")
# textReplace = text.replace('Ita', 'ITA')
# print(f"######## First 100 textReplace chars########\n{textReplace[0:100]}")
# print(f"######## find 'Python' in text########\n{text.find('Python')}")
# print(f"######## find 'Ita' in text ########\n{text.find('Ita')}")
# print(f"######## count 'Python' in text ########\n{text.count('Python')}")
# print(f"######## count 'Ita' in text ########\n{text.count('Ita')}")
# print(f"######## count 'Ita' in text ########\n{text.lower().count('ita')}")

# ToDo: Make a def that returns how many instances of some input words are present in an input text.


def countInText(word: str, text:str):
    word = word.lower()
    text = text.lower()
    return word, text.count(word)


def countWordsInText(wordsList:list, text:str):
    result = {}
    for item in wordsList:
        print(f"######\nItem: {item}")
        key, conteggio = countInText(item, text)
        print(f"Conteggio: {conteggio}")
        result[key] = conteggio
    return result


# words = ['frateLLI', 'ITalia', 'gatto']
# allWords = set(text.lower().replace('\n', ',').replace("'", " ").replace(';', ' '). replace('.', ' ').replace(',', ' ')
#                .replace('?', ' ').replace(':', ' ').replace('!', ' ').replace('  ', ' ').split(' '))
print(text.translate({ord("F"): ord(" "), ord("?"): ord(' ')})[0:100])
# print(allWords)
# conteggi = countWordsInText(allWords, text)
# print(conteggi)
# .....
# print(conteggi['ITalia'])
