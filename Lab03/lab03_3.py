import math

def f(x):
    return math.cos(2 * x)

def fp(x):
    return -2 * math.sin(2 * x)

def fpp(x):
    return -4 * math.cos(2 * x)
 
x = math.pi
print(f(x), fp(x), fpp(x))