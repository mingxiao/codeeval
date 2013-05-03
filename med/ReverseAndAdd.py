import sys

def palindrome(s):
    if len(s) <=1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

def reverse(n):
    return int(str(n)[::-1])

def process(n):
    r = reverse(n)
    idx = 0
    while not palindrome(str(n)):
        n = n+r
        r = reverse(n)
        idx +=1
    return idx,n


test_cases = open(sys.argv[1], 'r')
#test_cases  = open('ra.txt','r')
for test in test_cases.readlines():
    n = int(test.strip())
    tup = process(n)
    print tup[0],tup[1]

