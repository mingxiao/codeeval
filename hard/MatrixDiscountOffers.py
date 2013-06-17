'''
Created on May 4, 2013

@author: mingxiao10016
'''
import string
vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']

def score(product, customer):
    score = 0
    p_letters = len([c for c in product if c in string.ascii_letters])
    c_letters = len([c for c in customer if c in string.ascii_letters])
    if p_letters%2 == 0:
        num_vowels = len([c for c in customer if c in vowels])
        score = num_vowels*1.5
    else:
        score = len([c for c in customer if c not in vowels and c in string.ascii_letters])
    #now check if rule 3 applies
    if gcd(p_letters,c_letters) > 1:
        score *= 1.5
    return score    
    
def gcd(a,b):
    if b == 0:
        return a
    else: 
        return gcd(b,a%b)

def parse_input(testcase):
    cust = testcase.split(';')[0]
    prods = testcase.split(';')[1]
    cust = cust.split(',')
    prods = prods.split(',')
    assert len(cust) >0
    assert len(prods)>0
    return cust,prods        
    
INF = 100000000000000000

def hungarian(matrix):
    if len(matrix) != len(matrix[0]):
        matrix = squareit(matrix)
    global INF
    h, w,  = len(matrix), len(matrix[0]) 
    u, v, ind = [0]*h, [0]*w, [-1]*w
    for i in range(h):
        links, mins, visited = [-1]*w, [INF]*w, [False]*w
        markedI, markedJ, j = i, -1, 0
        while True:
            j = -1
            for j1 in range(h):
                if not visited[j1]:
                    cur = matrix[markedI][j1] - u[markedI] - v[j1]
                    if cur < mins[j1]:
                        mins[j1] = cur
                        links[j1] = markedJ
                    if j == -1 or mins[j1] < mins[j]: j = j1
            delta = mins[j]
            for j1 in range(w):
                if visited[j1]:
                    u[ind[j1]] += delta;  v[j1] -= delta
                else:
                    mins[j1] -= delta
            u[i] += delta
            visited[j] = True
            markedJ, markedI = j, ind[j] 
            if markedI == -1:
                break
        while True:
            if links[j] != -1:
                ind[j] = ind[links[j]]
                j = links[j]
            else:
                break
        ind[j] = i
    return [(ind[j], j) for j in range(w)]

def min_elem(matrix):
    min = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min:
                min = matrix[i][j]
    return min

def squareit(matrix):
    m = [row[:] for row in matrix]
    if len(m) != len(m[0]):
        minelem = min_elem(m)
        if len(m) > len(m[0]):
            ndiff = len(m) - len(m[0])
            for row in m:
                row += [minelem] * ndiff
        else:
            ndiff = len(m[0]) - len(m)
            for i in range(ndiff):
                m.append([minelem]*len(m[0]) )
    return m

def form_matrix(cust,prods):
    m = []
    for c in cust:
        r = []
        for p in prods:
            r.append(-1*score(p,c)) # multipy by -1 b/c we want the max
        m.append(r)
    return m

def ans(matrix,coors):
    result = 0
    for c in coors:
        if c[0] < len(matrix) and c[1] < len(matrix[0]):
            result += matrix[c[0]][c[1]]
    return -1*result

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    cust,prod = parse_input(test)
    m = form_matrix(cust,prod)
    coors = hungarian(m)
    result =ans(m,coors)
    print '%.2f'%result

test_cases.close()
