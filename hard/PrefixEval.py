#Sample code to read in test cases:

import sys

def eval(inputList):
    stack = []
    inputList.reverse()
#    print inputList
    for i in inputList:
#        print i
        if i.isdigit():
            #if its a number, cast it to an int and push it onto the stack
            stack.append(int(i))
        else:
            x = stack.pop()
            y = stack.pop()
            if i == '*':
                stack.append(x*y)
            elif i == '+':
                stack.append(x+y)
            else:
                stack.append(x/y)
    return stack.pop()

test_cases = open(sys.argv[1], 'r')
#test_cases = open("prefixInput.txt",'r')
for test in test_cases:
    if test == '\n':
        continue
    print eval(test.strip().split(" "))
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
