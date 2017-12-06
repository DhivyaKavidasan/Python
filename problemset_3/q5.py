'''
function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters
submitted by : dhivya.kavidasan
date: 05/12/2017
'''
def avoids(str,list1):

    list2=[]

   
    for i in str:

        list2.append(i)

    if len(set(list2) & set(list1))!=0:

        return False

    else:

        return True


str=raw_input("string")

list=raw_input("forbidden")

list1=[]
for i in list:

    list1.append(i)
print avoids(str,list1)

