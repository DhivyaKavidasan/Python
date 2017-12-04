'''
adding digits in alphanumeric string
submitted by: dhivya.kavidasan
date:3/12/2017
'''
def sum_digits(s):
  digitsum = 0
  for i in s:
    try:
        digitsum = digitsum + int(i)
        print digitsum
    except:
        pass 
  
s='a2b3c'
sum_digits(s)
