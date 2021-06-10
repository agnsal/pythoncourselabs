
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

# d = {
#     "category": "animal",
#     "name": "felix"
# }
# print(f"d: {d}")
# print(f"d['name']: {d['name']}")
#
# dd = {
#     "typology": {
#         "category": "animal",
#         "subcategory": "cat"
#     },
#     "name": "felix"
# }
# print(f"dd: {dd}")
# print(f"dd['typology']: {dd['typology']}")
# print(f"dd['typology']['subcategory']: {dd['typology']['subcategory']}")
#
# print(f"Is 'felix' in d? {'felix' in d}")
# print(f"Is 'felix' in d? {'felix' in d.values()}")
# print(f"d.values() {d.values()}")
# print(f"Is 'name' in d? {'name' in d}")
# print(f"Is 'name' in d? {'name' in d.keys()}")
# print(f"d.keys() {d.keys()}")
#
# d['colour'] = 'white'
# print(f"d: {d}")
#
# colour = d.pop('colour')
# print(f"colour: {colour}")
# print(f"d: {d}")
#
# del d['name']
# print(f"d: {d}")
#
# d.clear()
# print(f"d: {d}")

# ToDo: Uncomment the following piece of code, then print public values only and, finally, print email value.

x = {
    "id": "10024",
    "personal info": {
        "public": {
            "name": "Sara",
            "surname": "Rossi"
        },
        "private": {
            "date of birth": 1980,
            "gender": "F"
        }
    },
    "contacts": {
        "public": {
            "email": "sara@sara.it",
        },
        "private": {
            "phone": "+39xxxxxxxxxx"
        }
    }
}

xL4 = {
    "id": "10024",
    "general info": {
        "personal info": {
            "public": {
                "name": "Sara",
                "surname": "Rossi"
            },
            "private": {
                "date of birth": 1980,
                "gender": "F",
                "email": "test@email.com"
            }
        }
    },
    "contacts": {
        "public": {
            "email": "sara@sara.it",
        },
        "private": {
            "phone": "+39xxxxxxxxxx"
        }
    }
}

# print(x['personal info']['public'])
# print(x['contacts']['public'])
# print(x['contacts']['public']['email'])

# result = []
# result.append(x['personal info']['public'])
# result.append(x['contacts']['public'])
# result.append(x['contacts']['public']['email'])
# print("Result: ", result)

# resultPublics = []
# resultEmails = []


def ricorsioneSemplice():
    ui = input("Inserisci un valore: ")
    if ui.lower() == "ripeti":
        ricorsioneSemplice()
    else:
        print("Finito!")


def ricorsioneSempliceEsempio():
    ui = input("Inserisci un valore: ")
    if ui.lower() == "ripeti":
        ricorsioneSemplice()
    print("Finito!")


def generalExplorer(d: dict):
    assert isinstance(d, dict)
    for k in d:
        if not isinstance(d[k], dict):
            print("Foglia:", d[k])
        else:
            generalExplorer(d[k])


def explorer(x: dict, resultPublics=[], resultEmails=[]):
    assert isinstance(x, dict)
    for k in x:
        if k == "public":
            resultPublics.append(x[k])
        elif k == "email":
            resultEmails.append(x[k])
        if isinstance(x[k], dict):
            explorer(x[k])
    return {'publicItems': resultPublics, 'emailItems': resultEmails}

ricorsioneSemplice()

explorerResult = explorer(x)
print("ExplorerResult:", explorerResult)

generalExplorer(x)

# def printPublicOrEmail(d: dict):
#     for k in d:
#         if k == "public" or k == "email":
#             print(d[k])
#         if isinstance(d[k], dict):
#             printPublicOrEmail(d[k])
#
# printPublicOrEmail(x)

# for level1 in x:
#     if isinstance(x[level1], dict):
#         for level2 in x[level1]:
#             if level2 == "public":
#                 for info in x[level1][level2]:
#                     print(f"{info}: {x[level1][level2][info]}")
