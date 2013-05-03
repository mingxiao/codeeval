#Sample code to read in test cases:
#http://codeeval.com/open_challenges/52/
# see evernote CodeEval >> TextDollars

import sys

#spells one digit numbers
def spellOneDigit(numStr):
    num = int(numStr)
    return ones[num]

#spells out two digit numbers. It can handle leading zeros
def spellTwoDigit(numStr):
    if numStr in spec:
        return teens[int(numStr[1])]
    else:
        result = tens[int(numStr[0])] + spellOneDigit(numStr[1:])
        return result
    
#spells out three digit numbers. It can handle leading zeros
def spellThreeDigit(numStr):
    #if there is a leading zero, then fall back to spellTwoDigit
    if int(numStr[0]) == 0:
        return spellTwoDigit(numStr[1:])
    else:
        return ones[int(numStr[0])] +"Hundred"+ spellTwoDigit(numStr[1:])
    
#spells the number depending on the length of the number
def spellNumber(numStr):
    if len(numStr) == 3:
        return spellThreeDigit(numStr)
    elif len(numStr) == 2:
        return spellTwoDigit(numStr)
    else:
        return spellOneDigit(numStr)
    
#takes in a number as a string and return a list of the string split into groups of three in reverse order
#'12345' --> ['345','12']
def splitIntoThrees(line):
    n = 3
    line =line[::-1] #reverses string
    return [line[i:i+n][::-1] for i in range(0, len(line), n)]

def spellGroups(group):
    result = ""
    for i in range(len(group)):
#        print group[i]
#        print spellNumber(group[i])
        result = spellNumber(group[i]) + suffix[i] + result
    return result

def spellLine(line):
    group = splitIntoThrees(line)
    return spellGroups(group)

spec = ["10","11","12","13","14","15","16","17","18","19"]
ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen", "Seventeen","Eighteen","Nineteen"]
tens = ["","Ten","Twenty","Thirty","Forty", "Fifty", "Sixty", "Seventy","Eighty","Ninety"]
suffix = ["","Thousand","Million"]

test_cases = open(sys.argv[1], 'r')
#test_cases = open("input.txt",'r')
dollar = "Dollar"
dollars = "Dollars"
for test in test_cases:
    # skip the empty line
    if test=='\n':
        continue
    test = test.strip() #remove new line
    #special cases: 0,1
    if test == '0':
        print "Zero"+dollars
    elif test == '1':
        print "One"+dollar
    else:
        print spellLine(test)+dollars
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()