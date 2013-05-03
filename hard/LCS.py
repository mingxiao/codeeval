'''
Created on Jul 15, 2012

@author: mingxiao10016
'''

#constructs the table, n*m size.
# each element is of the form ((i,j),l), 
# where i,j is the index of its predecessor and l is the length at the current cell
def lcs(str1,str2):
    #add 1 because we need an initial row and column of null values
    #so when we are at table[i][j] we are referring to str1[i-1] and str2[j-1]
    n = len(str1)+1
    m = len(str2)+1
    table = [[(None,0)]*m for x in xrange(n)]
    for i in range(1,n):
        for j in range(1,m):
            if str1[i-1] == str2[j-1]:
                table[i][j] = ((i-1,j-1),table[i-1][j-1][1]+1)
            else:
                #they are not equal so we take the longest of the two previous
                if table[i-1][j][1] > table[i][j-1][1]:
                    table[i][j] = ((i-1,j),table[i-1][j][1])
                else:
                    table[i][j] = ((i,j-1),table[i][j-1][1])
    return print_LCS(table,str1,str2)

# given the table produces from lcs(), retrace the steps and produce the LCS
def print_LCS(table, str1,str2):
    result = ''
    n = len(str1)+1
    m = len(str2)+1
    curr = table[n-1][m-1]
    while curr[0] != None:
        prev_i = curr[0][0]
        prev_j = curr[0][1]
        prev = table[prev_i][prev_j]
        if prev[0] is None:
            return result
        if prev[0][0] == curr[0][0]-1 and prev[0][1] == curr[0][1]-1:
            result = str1[curr[0][0]-1] + result
        curr = prev
    return result

#Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = open('lcsInput.txt', 'r')
for test in test_cases:
    if test == '\n':
        continue
    test = test.strip()
    words = test.split(';')
    print lcs(words[0],words[1])

test_cases.close()
