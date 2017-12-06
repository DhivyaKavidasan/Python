'''
function called has_no_e that returns True if the given word doesn’t have the letter "e" in it.
submitted by : dhivya.kavidasan
date: 05/12/2017
'''
def has_no_e(str):
    if 'e' in str:
        print("False")
    elif 'E' in str:
        print("False")
    else:
        print("True")

str=raw_input("Enter a String:")
has_no_e(str)
'''