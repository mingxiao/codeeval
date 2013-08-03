import math
from sets import Set
from sys import maxint
import re

def dist(x1,y1,x2,y2):
    """
    Gives the distance, as the crow flies, between two points.
    """
    xdiff = x1-x2
    ydiff = y1-y2
    return math.sqrt(xdiff**2 + ydiff ** 2) 

def form_dists(coors):
    """
    Given a list of coordinates (as tuples), return the distance matrix
    """
    d = []
    for i in range(len(coors)):
        d.append([0]*len(coors))
    for i in range(len(coors)):
        for j in range(len(coors)):
            if i ==j :
                continue
            else:
                d[i][j] = dist(coors[i][0], coors[i][1], coors[j][0],coors[j][1])
    return d
            
def to_bitstr(length,lst):
    """
    Given the length, and a list of indices to turn on, return a 
    string rep of a bit mask.
    """
    s = ''
    for i in range(length):
        if i in lst:
            s+= '1'
        else:
            s += '0'
    return s

def k_subsets_i(n, k):
    '''
    Yield each subset of size k from the set of intergers 0 .. n - 1
    n -- an integer > 0
    k -- an integer > 0
    '''
    # Validate args
    if n < 0:
        raise ValueError('n must be > 0, got n=%d' % n)
    if k < 0:
        raise ValueError('k must be > 0, got k=%d' % k)
    # check base cases
    if k == 0 or n < k:
        yield set()
    elif n == k:
        yield set(range(n))

    else:
        # Use recursive formula based on binomial coeffecients:
        # choose(n, k) = choose(n - 1, k - 1) + choose(n - 1, k)
        for s in k_subsets_i(n - 1, k - 1):
            s.add(n - 1)
            yield s
        for s in k_subsets_i(n - 1, k):
            yield s

def k_subsets(s, k):
    '''
    Yield all subsets of size k from set (or list) s
    s -- a set or list (any iterable will suffice)
    k -- an integer > 0
    '''
    s = list(s)
    n = len(s)
    for k_set in k_subsets_i(n, k):
        yield set([s[i] for i in k_set])

def TSP(dists):
    """
    Given a matrix of distances, solve the travelling salesmen problem.
    Starting at vertex 0
    """
    route = {}
    best= {}
    #set the base cases
    nodes = len(dists)
    for i in range(nodes):
        S = to_bitstr(nodes,[0,i])
        if S not in best:
            best[S] = {}
            route[S] = {}
        best[S][i]= dists[0][i]
        route[S][i] = (to_bitstr(nodes,[0]),0)
    #recursive case
    for s in range(3,nodes+1):
        for sub in k_subsets(range(nodes),s):
            if 0 in sub:
                for j in sub:
                    if j != 0:
                        mincost = maxint
                        city = None
                        for i in sub:
                            if i != j and i!= 0:
                                s_copy = sub.copy()
                                s_copy.remove(j)
                                cstr = to_bitstr(nodes,s_copy)
                                cost = best[cstr][i]+ dists[i][j]
                                if cost < mincost:
                                    mincost = cost
                                    city = (cstr,i)
                        nstr = to_bitstr(nodes,sub)
                        if nstr not in best:
                            best[nstr] = {}
                            route[nstr] = {}
                        best[nstr][j] = mincost
                        route[nstr][j] = city
    beststr = to_bitstr(nodes,range(nodes))
    shortest =  min(best[beststr].values())
    for city,cost in best[beststr].iteritems():
        if cost == shortest:
            end_city = city
    return end_city,shortest,route
                                

def print_route(route,S,end):
    """
    Print the route starting from 0 to end.
    +1 because in codeeval problem statement, 
    index starts at 1
    """
    if end == 0:
        print end+1
    else:
        assert S in route
        print_route(route,route[S][end][0],route[S][end][1])
        print end+1


def get_coors(line):
    """
    Given a line of input, from codeEval, return
    a coordinate tuple (x,y)
    """
    regex = re.compile("[-]?\d+\.\d+")
    c = regex.findall(line)
    assert len(c) == 2
    return (float(c[0]),float(c[1]))


def file_to_coors(f):
    lines = open(f,'r')
    coors = []
    for line in lines:
        c = get_coors(line)
        coors.append(c)
    return coors


import sys
locations = file_to_coors(sys.argv[1])
dists= form_dists(locations)
end,scost,route = TSP(dists)
S = '1'*len(locations)
print_route(route,S,end)
