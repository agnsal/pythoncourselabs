
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

s = 'python'
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"s: {s}; len(s): {len(s)}")
print(f"l: {l}; len(l): {len(l)}")

s += " is a programming language"
l += [10, 11, 12, 13, 14, 15]

print(f"s: {s}; len(s): {len(s)}")
print(f"l: {l}; len(l): {len(l)}")
print(f"s[0]: {s[0]}")
print(f"l[0]: {l[0]}")
print(f"s[-1]: {s[-1]}")
print(f"l[-1]: {l[-1]}")
print(f"s[1:5]: {s[1:5]}")
print(f"l[1:5]: {l[1:5]}")
print(f"s[:3]: {s[:3]}")
print(f"l[:3]: {l[:3]}")
print(f"s[:-3]: {s[:-3]}")
print(f"l[:-3]: {l[:-3]}")
print(f"s[0:8:2]: {s[0:8:2]}")
print(f"l[0:8:2]: {l[0:8:2]}")
print(f"s[::-3]: {s[:-3]}")
print(f"l[::-3]: {l[:-3]}")

# ToDo: read a string from a text file and print its last 10 chars
