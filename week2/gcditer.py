
def gcdIter(a, b):
    if a > b:
        testvalue = b
    else:
        testvalue = a
    while a and b % testvalue != 0:
        testvalue -= 1
    return testvalue
print(gcdIter(2,12))
