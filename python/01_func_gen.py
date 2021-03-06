import random as rand

# Normal python function
def random(count):
    """
    Returns 'count' numbers of random integers in the range [0, 100]
    """
    ret = []
    while count>0:
        ret.append(rand.randint(0, 100))
        count -= 1
    return ret

# generator
def g_random(count):
    """
    Returns 'count' numbers of random integers in the range [0, 100]
    """
    while count>0:
        yield rand.randint(0, 100)
        count -= 1


# Lambda function - anonymous function
# lambda x: [ y*y for y in x ]


a = [1,2,3]
b = [5,6,7]

print a
print b
z =  zip(a,b)
print zip(*z)
c,d = zip(*z)

print c
print d

for i, j in z:
    print "%s - %s " % (i, j)




