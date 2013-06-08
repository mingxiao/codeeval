import sys

def score(x,y): 
    x = abs(x)
    y = abs(y)
    s = 0
    for i in str(x):
        s += int(i)
    for i in str(y):
        s += int(i)
    return s

def dpwalk(tol):
    """
    Dynammic programming solution. 
    (x,y) is reachable is (x,y) is valid and (x-1,y) reachable 
    or (x,y-1) reachable.

    Exploit symmetry by calculating from 0<= x,y <= 299. 
    Multiple solution by 4, and deduct double counts
    """
    reachable = {}
    reachable[(0,0)]= 1
    for i in range(299):
        for j in range(299):
            if i ==0 and j== 0:
                #base case
                continue
            elif i == 0:
                #boundary
                if score(i,j)<= tol and (i,j-1) in reachable:
                    reachable[(i,j)]= 1
                pass
            elif j== 0:
                #boundary
                if score(i,j) <= tol and (i-1,j) in reachable:
                    reachable[(i,j)] = 1
                pass
            else:
                #general
                if score(i,j) <= tol:
                    if (i-1,j) in reachable or (i,j-1) in reachable:
                        reachable[(i,j)] = 1
    count= len(reachable) *4
    count = count -3 #overcounted (0,0)
    count = count - 298*4 #overcounted the boundaries
    return count

print dpwalk(19)
