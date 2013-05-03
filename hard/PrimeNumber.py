'''
Created on Jul 18, 2012

@author: mingxiao10016
'''
import math
# sieve of erosthosthenes
def sieve(limit):
    table = [True] * limit                          
    table[0] = table[1] = False
    result = []
    for (i, isprime) in enumerate(table):
        if isprime:
            result.append(i)
            for n in range(2*i, limit, i):     
                table[n] = False
    return result

def print_table(table):
    result = ''
    for x in table:
        result += str(x)+','
    return result[:-1]

#Sample code to read in test cases:
import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = open('PrimeNumberInput.txt', 'r')
for test in test_cases:
    if test == '\n':
        continue
    test = test.strip()
    print print_table(sieve(int(test)))

test_cases.close()
