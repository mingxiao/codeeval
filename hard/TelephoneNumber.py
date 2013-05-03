'''
Created on Jul 16, 2012

@author: mingxiao10016
'''

mapping={'0':['0'],
         '1':['1'],
         '2':['a','b','c'],
         '3':['d','e','f'],
         '4':['g','h','i'],
         '5':['j','k','l'],
         '6':['m','n','o'],
         '7':['p','q','r','s'],
         '8':['t','u','v'],
         '9':['w','x','y','z'],
         }

def tele(result, rest):
    ans = []
    if rest == '':
        return [result]
    else:
        for ch in mapping[rest[0]]:
            ans += tele(result+ch,rest[1:])
    return ans

def tele_toString(teleList):
    result = ''
    for word in sorted(teleList):
        result += word + ','
    return result[:-1] #remove trailing comma

#Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == '\n':
        continue
    test =test.strip()
    print tele_toString(tele('',test))

test_cases.close()
