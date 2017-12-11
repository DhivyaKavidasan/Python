'''
function named test_square_root that prints a table 
submitted by :dhivya.kavidasan
date:06/12/2017
'''

import math
def newtonSqrt(a,x):
    
     y = (x + a/x) / 2
     return y
    
def tst_sqrt(a):
     y=math.sqrt(a)
     
     return y

def printt():
     print 'number\tnewtonsqrt\tsqrt\t\tdifference'
     for i in range(1,10):
         n=newtonSqrt(i,2.0)
         m=tst_sqrt(i)
         ab=n-m
         print "{:<6}\t{:<12}\t{:<12}\t{:}".format(i,n,m,ab)
printt()


