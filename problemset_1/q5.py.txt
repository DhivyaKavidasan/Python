'''
returning power and root of an integer
submitted by: dhivya.kavidasan
date:2/12/2017
'''
a = int(input('Enter an integer: '))

pwr = 1
root = 1
flag = False

while root <= a:
    if root**pwr == a:
        print('root =',root, 'power =', pwr)
        flag = True
    pwr = pwr + 1
    if pwr == 6:
        pwr = 1
        root = root + 1

if not flag:
    print('No such pair exist.')
