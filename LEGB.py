x = 100
def myFunc():
    x = 20
    def innerFunc():
        # global x
        print(x)
    innerFunc()


def outer():
    y = 20
    def inner():
        # nonlocal y
        y = 50
        print(y)
    inner()
    print(y)


# myFunc()
outer()

