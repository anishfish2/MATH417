def fpi(g,x0,n):
    # fixed point iteration to solve x = g(x)
    # x0 is the initial point
    # n is the number of iterations
    x = x0
    for j in range(n):
        print("x:", str(x))
        x = g(x)
    return x

# example: find the root of f(x)=x-cos(x) using fpi
import numpy as np
g = lambda x: 2 * np.cosh(x / 4)
x0, n = 8.5, 30
print(fpi(g,x0,n))
