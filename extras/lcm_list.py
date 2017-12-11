'''
finding lcm of list
submitted by: dhivya.kavidasan
date:6/12/2017
'''
def lcm(m, n):
  '''function to find lcm of two integers takes two integer values as parameters and returns value of lcm'''
  
  if m > n: 
    max = m 
  else: 
    max = n 
  try: 
    while(True): 
      if((max % m == 0) and (max % n == 0)): 
        lcm = max 
        return lcm 
        break 
        max=max+1 
  except Exception as e: 
        print e 
 
def test():
  '''test function to test reduce function'''
  list2=[4,8,12,16] 
  result=reduce(lcm,list2) 
  print result 
  list1=[3,6,8,0] 
  result=reduce(lcm,list1) 
  print result 
  
list3=[12,16,8,9] 
result=reduce(lcm,list3) 
print result 
test() 
