import sys
from test import Test


def printTest():
    print("test!!!!")
    return 4


def argsF(a, b, *args):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"type di args: {type(args)}")


def kwargsF(a, b, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"kwargs: {kwargs}")
    print(f"type di args: {type(kwargs)}")


def main(x):
    # t = Test(x)
    # kwargsF(b=1, a=2, c=3, z=4, l=5, y=6)
    pt = printTest
    # ...
    print(type(pt))
    pt()
    print(type(pt()))


if __name__ == "__main__":
    # print(sys.argv)
    # x = sys.argv[1]
    main("ciao")
