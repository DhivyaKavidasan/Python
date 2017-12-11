'''
function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list
submitted by : dhivya.kavidasan
date: 05/12/2017
'''
def uses_only(word, only_letters): 
  i = 0 
  while i <len(word): 
    if word[i] in only_letters: 
      i+=1 
    else: 
      return False 
    return True 
word='dhivya'
only_letters='xyz'
print uses_only(word,only_letters)