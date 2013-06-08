import re
def valid(s):
    regex = '[\w]+@[\w]+(\.[\w]+)+'
    pat =re.compile(regex)
    m = pat.match(s)
    if m is not None:
        return True
    else:
        return False

import sys

test_cases = open(sys.argv[1],'r')

for t in test_cases:
    if valid(t.strip()):
        print 'true'
    else:
        print 'false'
