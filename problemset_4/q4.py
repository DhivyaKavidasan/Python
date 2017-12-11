''''
printing triangular pattern of asterisks
submitted by: dhivya.kavidasan
date: 10/12/2017
'''
#non recursive method
def tri(n):
  for i in range(1,n):
    print (' '*(n-i)+'*'*i+'*'*i)
n=int(raw_input("enter a number:"))
tri(n)
