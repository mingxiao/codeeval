
def mlast(lst,i):
    return lst[-i]

import sys

tcases = open(sys.argv[1],'r')
for t in tcases:
    t=t.strip()
    lst = t.split(' ')
    idx = int(lst.pop())
    if idx <= len(lst):
        print mlast(lst,idx)
