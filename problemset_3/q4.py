'''
program to print only the words that have no “e” and compute the percentage of the words in the list have no “e.”
submitted by : dhivya.kavidasan
date:5/12/2017
'''
def has_no_e(strlist):
    with_e=[]
    without_e=[]
    for i in strlist:
        if 'e' in i:
            with_e.append(i)
        elif 'E' in i:
            with_e.append(i)
        else:
            without_e.append(i)
    print "words without e:", without_e
    original_len=float(len(strlist))
    len_with_e=float(len(with_e))
    len_without_e=float(len(without_e))
    percentage=(len_without_e/original_len)*100
    print "percentage of list that have no 'e':",percentage
string=raw_input("str")
strlist=string.split()
has_no_e(strlist)
