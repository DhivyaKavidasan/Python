'''
string comparision without built in function
submitted by: dhivya.kavidasan
date: 02/12/2017
'''

x=raw_input('Enter string 1: ')  
y=raw_input('Enter string 2: ')  

def isIn(x,y):  
    if x in y or y in x:  
       print True  
    else:   
        print False  
isIn(x,y)