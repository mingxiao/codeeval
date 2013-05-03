import re
import operator

"""
Currently takes too long!! Need a better data structure than a hash table.
Maybe a heap would work better?
"""

def findall_idx(s,pat):
    """
    Returns all start indices where substring pat appears in s, if at all
    """
    return [m.start() for m in re.finditer(pat,s)]

def reaches_end(s1,s2,pos):
    """
    Returns True if s2 overlaps s1 on the right, starting at position pos in
    s1
    """
    #print s1[pos:]
    t = len(s1) -pos
    #print s2[:t]
    return s1[pos:] == s2[:t]

def overlap(s1,s2):
    """
    Returns lenght of max overlap if we were to stitch s2 to the right of s1
    """
    #loop over s2 from left to right and check for overlap
    for i in range(len(s2),0,-1):
        idxs = findall_idx(s1,s2[:i])
        if len(idxs) == 0:
            continue
        mx = max(idxs)
        if reaches_end(s1,s2,mx):
            return i
    return 0

def combine(s1,s2,pos):
    """
    Stitches s2 to the right of s1 at position pos
    """
    return s1[:-pos]+s2        

def split_input(st):
    return st.split(';')    

def max_item(h):
    item = max(h.iteritems(), key=operator.itemgetter(1))
    return item

def remove(d,k1,k2):
    """
    In dictionary d, remove any key where key[0] equals k1 or key[1] equals k2
    """
    c = d.copy()
    for key in d.iterkeys():
        if key[0] == k1 or key[1] == k2:
            del c[key]
    return c

def remove_fromlist(x,item):
    """
    should also remove items that are a substring of item
    """
    clist = list(x)
    return filter(lambda a: a != item or not a in item, clist)

def create_dict(lines):
    """
    Given lines of string create a dictionary that maps from (s1,s2) --> int
    for each pair of strings in lines
    """
    d = {}
    for s1 in lines:
        for s2 in lines:
            if s1 == s2:
                continue
            ov = overlap(s1,s2)
            if ov >0:
                d[(s1,s2)] = ov
    return d

def solve(strinput):
    #split input to get separate strings
    lines = split_input(strinput)
    oldlen = len(lines)
    while len(lines) > 1:
        print '=================='
        d = create_dict(lines)
        #print d
        try:
            (words,value) = max_item(d)
            new_word = combine(words[0],words[1],value)
            lines = remove_fromlist(lines,words[0])
            lines = remove_fromlist(lines,words[1])
            lines.append(new_word)
        except ValueError:
            """
            Kind of a dinky hack, but if we get an error in max_items, then we know
            there are no more matches, so choose the longest length string as our answer
            """
            return max(lines, key=len)
    return lines[0]


import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    print solve(test)
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
    
