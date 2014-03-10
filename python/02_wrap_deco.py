import math

# Wrapped function
def power(name, c):
    def func(n):
        print("{} of {} is {}".format(name, n, math.pow(n, c)))
    return func


square = power("Square", 2)
cube = power("Cube", 3)

print square
print cube

square(5)
cube(5)
