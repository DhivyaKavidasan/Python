'''
evaluating the user input
submitted by: dhivya.kavidasan
date:3/12/2017
'''
def eval_loop():
    while True:
        a = raw_input('enter the expression to be evaluated: ')
        if a == 'done':
            break
        else:
            result = eval(a)
            print result
eval_loop()