''' 
palindrome check
submitted by: dhivya.kavidasan 
date:5/12/2017 
''' 
def is_palindrome(s): 
  reverse = [] 
  for c in s: 
    reverse.append(c) 
  return reverse == reverse[::-1] 
s=raw_input("enter a string") 
print is_palindrome(s) 
