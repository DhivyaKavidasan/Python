'''
adding decimal numbers
submitted by: dhivya.kavidasan
date:2/12/2017
'''
s = '1.23,2.4,3.123'
total = 0
s=s.split(',')
for i in s:
    total = total + float(i)
print total
