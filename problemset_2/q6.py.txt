'''
printing the first even number in the list
submitted by: dhivya.kavidasan
date:3/12/2017
'''

def isEven(l):
  for i in l:
    if i % 2 == 0:
      print i, " is the first even number in the list"            
      exit()
  raise ValueError("No even numbers in list!")
l=[3,4,6,8]
isEven(l)