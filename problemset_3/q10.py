'''
function called is_anagram that takes two strings and returns True if they are anagrams
submitted by:dhivya.kavidasan
date: 06/12/2017
'''

def is_anagram(list1,list2): 
     list3=[] 
     list4=[] 
     list1.sort() 
     list2.sort() 
     for i in list1: 
         list3.append(i) 
     for j in list2: 
         list4.append(j) 
     c=(''.join(list3)) 
     d=(''.join(list4)) 
     if c==d : 
         return True 
     else: 
         return False 
str1=raw_input("enter STRING 1") 
list1=[] 
for i in str1: 
     list1.append(i) 
str2=raw_input("enter STRING 2") 
list2=[] 
for i in str2: 
     list2.append(i) 

 
print is_anagram(list1,list2) 
