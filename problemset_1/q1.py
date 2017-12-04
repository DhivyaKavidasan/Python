
'''
greatest of three odd numbers
submitted by: dhivya.kavidasan
date:2/12/2017
'''
def odd_check(a):
  if a%2 != 0:
    return a
def great(a,b):
  if a>b:
    return a
  else:
    return b
  
def main(x,y,z):
  x=odd_check(x)
  y=odd_check(y)
  z=odd_check(z)
  if x and y and z:
    print (great(x,great(y,z)))
    
  elif x and y and not z:
    print (great(x,y))
  elif x and z and not y:
    print (great(x,z))
  elif z and y and not x:
    print (great(z,y))
  elif x and not y and not z:
    print x
  elif y and not x and not z:
    print y
  elif z and not y and not x:
    print z
  else:
    print ("none are odd")

x=raw_input("enter a number")
y=raw_input("enter a number")
z=raw_input("enter a number")
x=int(x)
y=int(y)
z=int(z)
main(x,y,z)



