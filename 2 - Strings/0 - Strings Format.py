
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

s = "hello"
x = "Python"
y = "!!!"
i = 100

# print(s + " Python" + "!!!")
# print(s + " Python" + "!!!" + str(1))
# print((s + ' ') * 3 + " Python" + "!" * 10)
# print("hello %(x)s%(y)s" % {"x": "Python", "y": "!!!"})
# print("hello {0}{1}".format(x, y))
# print("hello {1} !!!!! {0}".format(x, y))
# print("hello {x}{y} ____ {x}{x} {x}".format(x="Pluto", y="???"))
print(f"hello {x}{y} integer!!! {i}")
print(f"hello {x}{y} integer!!! {{{i}}}")

# ToDO: Format strings coming from user inputs.
