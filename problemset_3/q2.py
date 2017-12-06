'''
function called rotate_word() that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string "rotated" by the given amount
submitted by : dhivya.kavidasan
date: 05/12/2017
'''
def rotate_word(s,n):
     a=[]
     b=[]
     c=[]
     for i in s:
         a.append(ord(i))
         
     for i in a:
         b.append(i+n)    
         
     for i in b:
         c.append(chr(i))
     print c   

s=raw_input("Enter the word")
n=raw_input("Enter the no by which you want to rotate:")
n=int(n)
rotate_word(s,n)
