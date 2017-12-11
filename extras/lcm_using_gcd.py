'''
finding lcm of two integers using gcd
submitted by: dhivya.kavidasan
date:6/12/2017
'''
def gcd(a, b):
  '''function to find gcd of two integers takes integers as parameters an returns gcd value'''

  if a==b:
    return a
  if a > b:
      r = a % b
      if r == 0:
          return b
      else:
          return gcd(b, r)
  if a < b:
    r = b % a
    if r == 0:
      return a
    else:
      return gcd(a, r)
            
def test():
  '''test function to test gcd(a,b)'''
  
  print ("\n------TEST FUNCTION------")
  print gcd(2,4), "\t expected result is 2"
  
n1=raw_input("enter first number")     #userinput
n2=raw_input("enter second number")    #userinput
n1=int(n1)
n2=int(n2)
lcm=n1*n2/gcd(n1,n2)      #formulae to find LCM using GCD
print("LCM of two numbers:",lcm)
test()

