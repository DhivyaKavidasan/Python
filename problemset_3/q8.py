'''
Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok)
submitted by : dhivya.kavidasan
date: 05/12/2017
'''

def is_abcedarian(word):
  
  j=0
  for i in word:
    if word[j+1] >= word[j]:
        return True
    else:
        return False

word='aux'
print is_abcedarian(word)
