'''
Created on Jul 20, 2012

@author: mingxiao10016
'''

def maxSum(numbers):
    S = [0] * len(numbers)
#    print S
    S[0] = numbers[0]
    for i in range(1,len(numbers)):
        S[i] = max(S[i-1]+numbers[i],numbers[i])
#        print i,numbers[i]
#    print S
    return max(S)


#Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = open('sumInput.txt','r')
for test in test_cases:
    if test =='\n':
        continue
    test = test.strip()
#    print test.split(',')
    nums = [int(x) for x in test.split(',')]
    print maxSum(nums)
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
