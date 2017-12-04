'''
checking for the palindrome string
submitted by: dhivya.kavidasan
date:3/12/2017
'''
def is_palindrome(s):
  reverse = []
  for c in s:
    reverse.append(c)
  return reverse == reverse[::-1]
s=raw_input("enter a string")
print is_palindrome(s)
 