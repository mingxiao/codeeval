#Sample code to read in test cases:
#Note: Issue with eval(). eval('011') results in 9, because '011' is treated as OCTAL
# Solved using regex to remove all leading 0s, except those that at just all 0s

# Issue 2: it currently takes TOO long!
# could we memotize this?

import re
import sys

#our look up table. The keys are strings to be evaluated and the value is their computed result
# "1+2" => "3"
global lookUp
lookUp = {}
primes = [2,3,5,7]
def isUgly(number):
    for p in primes:
        if number % p == 0:
            return True
    return False
    
    
# this is correct, but too SLOWWW ========
def func(seen, remaining):
    global numUgly
    if remaining == '':
        # we've seen all the strings so evaluate what we have seen
        seen = re.sub(r'\b0+(?!\b)', '', seen)
        n = eval(seen)
        if isUgly(n):
#            print n
            numUgly += 1
#            print 'seen',seen,n
#        print n
    else:
        func(seen+remaining[0],remaining[1:])
        func(seen+"+"+remaining[0],remaining[1:])
        func(seen+"-"+remaining[0],remaining[1:])
        
def func_driver(string):
    func(string[0],string[1:])
    
# =+++++++++++++++++++++++


# divide and conquer algorithm, akin to merge sort but with memoization. Split the number in half.
# When we merge, we evaluate the halves by putting a plus, minus, or nothing in between.

# This approach is faster, but not fast enough. On 13 digit input, this takes 10+ seconds
def part(evalStr):
    global lookUp
#    print evalStr
#    val =lookUp.get(evalStr,None)
#    if val is not None:
#        return val
    if len(evalStr) == 1:
        lookUp[evalStr] = evalStr
        return evalStr
    else:
        
        #split in half with a plus,minus, and nothing in between
        half = len(evalStr)/2
        left = evalStr[0:half]
        right = evalStr[half:]
        
        # putting nothing in between
#        tmp = re.sub(r'\b0+(?!\b)', '', evalStr) #gets rid of leading 0s
#        num = eval(tmp)
#        lookUp[evalStr] = str(num) #cast to a string (cause other sub expressions may use it
        
        leftList = part(left)
        rightList = part(right)
#        print "left", leftList
#        print "right", rightList
        return merge(leftList,rightList)
        # the following is the merge step, should be in its own method.
        
        
def merge(leftList,rightList):
    result = []
    for l in leftList:
            for r in rightList:
                l_new = l
                r_new = r
                # if we've seen this expression before, then just get its value
                if l in lookUp:
                    l_new = lookUp[l]
#                    print 'newL'
                if r in lookUp:
                    r_new = lookUp[r]
#                    print 'newR'
#                print 'old',l,r
#                print 'new',l_new,r_new
#                print lookUp
                tmp1 = l+r #put nothing in between (still use the old value)
                tmp2 = l_new+"+"+r_new #put a plus in between
                tmp3 = l_new+"-"+r_new # put a minus in between
                
                if tmp1 in lookUp:
#                    print tmp1
#                    print 'here1'
                    # if we've seen this particular chunk, the get the value from lookUp
                    result.append(lookUp[tmp1])
#                    print tmp1,lookUp[tmp1]
                else:
                    tmp1_post = re.sub(r'\b0+(?!\b)', '', tmp1) #gets rid of leading 0s in expression
                    tmp1_eval = eval(tmp1_post)
                    lookUp[tmp1] = str(tmp1_eval)
                    result.append(tmp1)
                    
                if tmp2 in lookUp:
#                    print 'here2'
                    result.append(lookUp[tmp2])
#                    print tmp2,lookUp[tmp2]
                else:
                    tmp2_post = re.sub(r'\b0+(?!\b)', '', tmp2) #gets rid of leading 0s in expression
                    tmp2_eval = eval(tmp2_post)
                    lookUp[tmp2] = str(tmp2_eval)
                    result.append(tmp2)
                    
                if tmp3 in lookUp:
#                    print 'here3'
                    result.append(lookUp[tmp3])
#                    print tmp3,lookUp[tmp3]
                else:
                    tmp3_post = re.sub(r'\b0+(?!\b)', '', tmp3) #gets rid of leading 0s in expression
                    tmp3_eval = eval(tmp3_post)
                    lookUp[tmp3] = str(tmp3_eval)
                    result.append(tmp3)
#    print result
    print tmp1,tmp2,tmp3,lookUp
    return result
        
def countUglie(uglyList):
    result = 0
    for exp in uglyList:
        exp = re.sub(r'\b0+(?!\b)', '', exp) #gets rid of leading 0s in expression
        num= eval(exp)
#        print num
        if isUgly(num):
#            print num
            result +=1
    return result
#        
#test_cases = open("uglyInput.txt",'r')
##test_cases = open(sys.argv[1], 'r')
#lookUp = {}
#for test in test_cases:
#    if test == '\n':
#        continue
#    test=test.strip()
#    l = part(test)
#    n = countUglie(l)
#    print n
#    print test
#    func_driver(test)
#    print numUgly

#test_cases.close()
