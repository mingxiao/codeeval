import re

def findall(s,f):
    return [m.start() for m in re.finditer(f, s)]

def findfirst(s,f,idx):
    """
    Returns the first index of f in s where index >= idx
    """
    a = findall(s,f)
    l = [x for x in a if x >= idx]
    if len(l) == 0:
        return None
    else:
        return l[0]

def available(used,start,end):
    #print 'AVAIL',used[start:end]
    for i in range(start,end):
        if used[i] == 1:
            return False
    return True

def replace_atidx(s,f,r,idx):
    """
    replaces
    """
    return s[:idx]+r+s[idx+len(f):]

def redo_used(used,start, flen,rlen):
    return used[:start]+[1]*rlen+used[start+flen:]

def sub2(s,used,f,r):
    idx = findfirst(s,f,0)
    #print s,f,idx,used
    while idx is not None:
        s_old = s
        if available(used,idx,idx+len(f)):
            #print f, s[idx:idx+len(f)]
            s = replace_atidx(s,f,r,idx)
            used = redo_used(used,idx,len(f),len(r))
            #print s, used
            idx = findfirst(s,f,idx+len(r))
            #print idx
        else:
            idx = findfirst(s_old,f,idx+len(f))
    return s,used

def sub(s,used,f,r):
    """
    Replaces all occurences of f in s with r, if those indices has not been
    used already. (used is a list, used[4]=1 mean s[4] has already been
    replaced
    """
    #ISSUE
    idx = findall(s,f)
    # we need to change this every time,since we're constantly changing our string
    print f,idx
    flen = len(f)
    for i in idx:
        if available(used,i,i+flen):
            print f, s[i:i+flen]
            print i,used[i:i+flen], r
            s = replace_atidx(s,f,r,i)
            used = redo_used(used,i,len(f), len(r))
    return s,used

def form(tcase):
    x = tcase.split(';')
    return x[0],x[1].split(',')

def answer(tcase):
    """
    tcase is the test case
    """
    #print '=============='
    s, slist = form(tcase)
    assert len(slist)%2 ==0
    used = [0]*len(s)
    for i in range(len(slist)/2):
        s,used = sub2(s,used,slist[2*i],slist[2*i+1])
    return s

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    t = test.strip()
    #print t
    print answer(t)

test_cases.close()


