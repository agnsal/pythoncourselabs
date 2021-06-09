
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

# l = [0, 1, 2, 3, 4, 5]
# print(f"l: {l}; len(l): {len(l)}")
# print(f"l[0]: {l[0]}; type(l[0]): {type(l[0])}")
#
# ll = [[0, 1], [2, 3], [4, 5]]
# print(f"ll: {ll}; len(ll): {len(ll)}")
# print(f"ll[0]: {ll[0]}; type(ll[0]): {type(ll[0])}; len(ll[0]): {len(ll[0])}")
# print(f"ll[0][0]: {ll[0][0]}; type(l[0][0]): {type(ll[0][0])}")
#
# myList = list()  # Equivale a myList = []
# print(f"myList: {myList}; len(myList): {len(myList)}")
# myList.append(0)
# myList.extend([20.56, 12, 12])
# print(f"myList: {myList}; len(myList): {len(myList)}")
# myList.pop(-1)  # Equivale a lyList.pop()
# print(f"myList: {myList}; len(myList): {len(myList)}")
# myList.append('python')
# print(f"myList: {myList}; len(myList): {len(myList)}")
# myList.remove('python')
# print(f"myList: {myList}; len(myList): {len(myList)}")
# myList.insert(0, 3)
# print(f"myList: {myList}; len(myList): {len(myList)}")
# print(f"Is 4 in myList? {4 in myList}")
# print(f"myList index of 12: {myList.index(12)}")
# myList.reverse()
# print(f"Reverse of myList: {myList}")
# myList.sort()
# print(f"Sort of myList: {myList}")
#
#
# myListEqual = myList
# print(f"myListEqual: {myListEqual}")
# myListEqual.append(100)
# print(f"myList: {myList}")
# print(f"myListEqual: {myListEqual}")
#
# myListCopy = myList.copy()
# print(f"myListCopy: {myListCopy}")
# myListCopy.append(100)
# print(f"myList: {myList}")
# print(f"myListCopy: {myListCopy}")

# ToDo: Cycle inside l and copy all its values inside another list.


l = [0, 1, 2, 3, 4, 5]


def copyList(l: list):
    ll = []
    for li in l:
        ll.append(li)
    return ll

print(copyList(l))


def shortCopy(l: list):
    return [item for item in l]

lCopy = shortCopy(l)
print(lCopy)
