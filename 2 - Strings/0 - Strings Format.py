s = "hello"
x = "Python"
y = "!!!"

print(s + " Python" + "!!!")
print("hello %(x)s%(y)s" % {"x": "Python", "y": "!!!"})
print("hello {0}{1}".format(x, y))
print("hello {1} {0}".format(x, y))
print("hello {x}{y}".format(x="Pluto", y="???"))
print(f"hello {x}{y}")

# ToDO: Format strings coming from user inputs.
