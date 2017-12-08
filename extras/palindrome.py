'''
palindrome without stepsize
submitted by:dhivya.kavidasan
date:08/12/2017
'''

def isPalindrome(s):
  '''function to check palindrome takes string as a parameter
  and returns boolean'''
  
  length=len(s)
  i=0
  while(length>0):
    if s[i]==s[length-1]:
      i=i+1
      length=length-1
    else:
      return False
  return True
  
def test():
  '''testfunction to check isPalindrome function'''
  
  print "------test function-------"
  print isPalindrome("malayalam"), "\t expected result is true"
  print isPalindrome("tamil"),"\t expected result is false"
  
s=raw_input("enter a string:")
'''gets the string from the user'''

print isPalindrome(s)
test()
