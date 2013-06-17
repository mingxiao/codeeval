import math

def num_double_squares(n):
    """
    Returns the number of ways a number can be represented as a double square
    """
    i = 0
    j = int(1+math.sqrt(n))
    ans = 0
    while i <= j:
        s = i*i + j*j
        if s < n:
            i+=1
        elif s > n:
            j-=1
        else:
            ans+=1
            i+=1
            j-=1
    return ans

import sys
testcases= open(sys.argv[1],'r')
numtest = int(testcases.readline().strip())
for i in range(numtest):
    n = testcases.readline().strip()
    print num_double_squares(int(n))

testcases.close()
