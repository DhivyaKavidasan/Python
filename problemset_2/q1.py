'''
finding gcd of two integers
submitted by: dhivya.kavidasan
date:2/12/2017
'''
def gcd(a, b):
    if a > b:
        r = a % b
        if r == 0:
            print b
        else:
            return gcd(b, r)
    if a < b:
        r = b % a
        if r == 0:
            print a
        else:
            return gcd(a, r)
n1=raw_input("enter first number")
n2=raw_input("enter second number")
n1=int(n1)
n2=int(n2)
gcd(n1,n2)