
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
#     "name": "cat"
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
#
# d['colour'] = 'white'
# print(f"d: {d}")
#
# colour = d.pop('colour')
# print(f"colour: {colour}")
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
            "gender": "F",
            "test": {
                "public": {
                    "newLevel": 10,
                    "x": {
                        "y": {
                            "z": 1
                        }
                    }
                }
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

# def test():
#     print("Sono la funzione di test")
#     test()
#
# test()

def ricerca(daCercare, dizionario):
    for k, v in dizionario.items():
        # if k == "public" or k == "email":
        if k in daCercare:
            print(f"key: {k} - val: {v}")
        if isinstance(v, dict):
            for k1, v1 in v.items():
                if k1 in daCercare:
                    print(f"key_1: {k1} - val_1: {v1}")
                if isinstance(v1, dict):
                    for k2, v2 in v1.items():
                        if k2 in daCercare:
                            print(f"key_2: {k2} - val_2: {v2}")


# def check(item, val, l):
#     if item not in l:
#         print(f"key: {item} - val: {val}")

# def ricercaE(daEvitare, dizionario):
#     for k, v in dizionario.items():
#         check(k, v, daEvitare)
#         if isinstance(v, dict):
#             for k1, v1 in v.items():
#                 check(k1, v1, daEvitare)
#                 if isinstance(v1, dict):
#                     for k2, v2 in v1.items():
#                         check(k2, v2, daEvitare)
#
#
# cercati = ["public", "email"]
# evitati = ["test", "email", "private", "public"]
# risultato = ricercaE(evitati, x)


def naviga(d, f):
    assert isinstance(d, dict)
    for k, v in d.items():
        if k not in f:  # Tutti
            print(f"k: {k} - v: {v}")
        if isinstance(v, dict):
            naviga(v, f)
        # else:  # Foglie
        #     if k not in f:
        #         print(f"k: {k} - v: {v}")


indesiderati = ["test", "email", "public", "private"]
naviga(x, indesiderati)
