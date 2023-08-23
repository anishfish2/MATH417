import math
import sys

def bisection(func, a, b, tol, maxIt):
    count = 0
    while (b - a) / 2 > tol and count < maxIt:
        p = (b + a) / 2
        if func(p) == 0:
            return p
        if func(a) * func(p) < 0:
            b = p
        else: 
            a = p
        count += 1
    return p


def main():
    func = lambda x: x ** 2 - 2
    a, b, tol, maxIt = 0, 2, 10 ** (-5), 1000000

    # a = sys.argv[1]
    # b = sys.argv[2]
    # tol = sys.argv[3]

    print(bisection(func, a, b, tol))


if __name__ == "__main__":
    main()



