'''
dividing values in two list of equal length 
submitted by:dhivya.kavidasan
date:03/12/2017
 ''' 
def getratio(vect1,vect2):
  ratio=[]
  for i in range(len(vect1)):
    a=float(vect1[i])
    b=float(vect2[i])
    ratio.append(a/b)
  return ratio
l1=[4,8,12,16]
l2=[2,4,8,4]
print getratio(l1,l2)
