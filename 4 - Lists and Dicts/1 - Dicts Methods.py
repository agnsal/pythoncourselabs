
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

# print(f"Is 'felix' in d? {'felix' in d}")
# print(f"Is 'felix' in d? {'felix' in d.values()}")
# print(f"d.values() {d.values()}")
# print(f"Is 'name' in d? {'name' in d}")
# print(f"Is 'name' in d? {'name' in d.keys()}")
# print(f"d.keys() {d.keys()}")

# d['colour'] = 'white'
# print(f"d: {d}")

# colour = d.pop('colour')
# print(f"colour: {colour}")
# print(f"d: {d}")

# d.clear()
# print(f"d: {d}")

# ToDo: Uncomment the following piece of code, then print public values only and, finally, print email value.

x = {
    "id": "10024",
    "personal info": {
        "public": {
            "name": "Sara",
            "surname": "Rossi",
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

# print(x["personal info"]["public"])
# print(x["contacts"]["public"])
# print(x["contacts"]["public"]["email"])

# def partialPrint(d:dict):
#     for el in d:
#         if isinstance(d[el], dict):
#             partialPrint(d[el])
#             continue
#         if el == 'email':
#             print(d[el])

def partialPrint(d:dict):
    for el in d:
        if isinstance(d[el], dict) and el != "public":
            partialPrint(d[el])
            continue

        if el == 'email':
            print(d[el])
            continue

        if el == 'public':
            for el2 in d[el]:
                print(d[el][el2])


partialPrint(x)
