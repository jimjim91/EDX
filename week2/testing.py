
"""
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    for n in range(exp):
        result *= base
        print (result)
    return result

print (iterPower(10,4))
"""
def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)
print (recurPower(10,4))
