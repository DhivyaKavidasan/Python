'''
function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise
submitted by : dhivya.kavidasan
date: 05/12/2017
'''

def is_sorted(s):
  j=0
  for i in s:
    if s[j+1] >= s[j]:
        return True
    else:
        return False

s = '122'
print is_sorted(s)
