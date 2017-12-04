'''
finding out whether a is power of b or not
submitted by: dhivya.kavidasan
date:2/12/2017
'''
def is_power(a,b):
    if a == b:
        return True
    if a % b == 0 and is_power(a/b,b):
        return True
    return False
print is_power(4,2)

