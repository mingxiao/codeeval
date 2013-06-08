
def solve(matrix):
    #dynammic programming solution
    n = len(matrix)
    ans = [[0 for i in xrange(n)] for j in xrange(n)]
    for r in range(n):
        for c in range(n):
            if r ==0 and c ==0:
                ans[r][c] = matrix[r][c]
            elif r == 0:
                ans[r][c] = ans[r][c-1]+matrix[r][c]
            elif c == 0:
                ans[r][c] = ans[r-1][c]+matrix[r][c]
            else:
                ans[r][c] = min(ans[r-1][c]+matrix[r][c],
                                ans[r][c-1]+matrix[r][c])
    return ans[n-1][n-1]

def form_matrix(lines):
    m = []
    for line in lines:
        s = [int(x) for x in line.strip().split(',')]
        m.append(s)
    return m

import sys
t = open(sys.argv[1],'r')
l = t.readline().strip()
while len(l) != 0:
    n = int(l)
    mlines = []
    for i in range(n):
        mlines.append(t.readline().strip())
        pass
    matrix = form_matrix(mlines)
    print solve(matrix)
    l= t.readline().strip()
