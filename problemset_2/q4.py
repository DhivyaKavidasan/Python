'''
converting binary to decimal
submitted by:dhivya.kavidasan
date:03/12/2017
 ''' 
def B2D(a):
  decimal=0
  for i in a:
    decimal=decimal*2+ int(i)
  return decimal
print B2D('10011')
  