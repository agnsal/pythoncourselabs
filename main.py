import sys
from test import Test


def main(x):
    t = Test(x)


if __name__ == "__main__":
    print(sys.argv)
    x = sys.argv[1]
    main(x)
