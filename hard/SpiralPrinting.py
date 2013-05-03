'''
Created on Jul 18, 2012

@author: mingxiao10016

Starting from the upper left point, spiral printing follows theses rules in order of precedence:

print all the way right,
print all the way down,
print all the way left,
print all the way up.
 
We repeatily apply those rules until all cells have been printed
'''

def canPrintRight(visited, pos,n,m):
    x = pos[0]
    y = pos[1]
    return y+1 < n and visited[x][y+1] is False

def canPrintDown(visted,pos,n,m):
    x = pos[0]
    y = pos[1]
    return x+1 < n and visited[x+1][y] is False

def canPrintLeft(visited,pos,n,m):
    x = pos[0]
    y = pos[1]
    return y-1 >= 0 and visited[x][y-1] is False

def canPrintUp(visited,pos,n,m):
    x = pos[0]
    y = pos[1]
    return x-1 >=0 and visited[x-1][y] is False
    

# given the starting position, print all the way right.
# return the position of the last printed cell (x,y)
def printRight(table,visited,start,rows,cols):
    x = start[0]
    y = start[1]
    while y+1 < cols and visited[x][y+1] is False:
        print table[x][y+1],
        visited[x][y+1] = True
        y = y+1
    return (x,y)

def printDown(table,visited,start,rows,cols):
    x = start[0]
    y = start[1]
    while x+1 < rows and visited[x+1][y] is False:
        print table[x+1][y],
        visited[x+1][y] = True
        x = x+1
    
    return (x,y)

def printLeft(table,visited,start,rows,cols):
    x = start[0]
    y = start[1]
    while y-1 >= 0 and visited[x][y-1] is False:
        print table[x][y-1],
        visited[x][y-1] = True
        y = y-1
    return (x,y)

def printUp(table,visited,start,rows,cols):
    x = start[0]
    y = start[1]
    while x-1 >= 0 and visited[x-1][y] is False:
        print table[x-1][y],
        visited[x-1][y] = True
        x = x-1
    return (x,y)

def spiralPrint(table,visited,cur,rows,cols):
    print table[cur[0]][cur[1]],
    visited[cur[0]][cur[1]]= True
    while cur != None:
#        print cur,'here'
        if canPrintRight(visited,cur,rows,cols):
            cur = printRight(table,visited,cur,rows,cols)
#            print cur,1
        elif canPrintDown(visited,cur,rows,cols):
            cur = printDown(table,visited,cur,rows,cols)
#            print cur,2
        elif canPrintLeft(visited,cur,rows,cols):
            cur = printLeft(table,visited,cur,rows,cols)
#            print cur,3
        elif canPrintUp(visited,cur,rows,cols):
            cur = printUp(table,visited,cur,rows,cols)
#            print cur,4
        else:
#            print cur, "none"
            cur = None
#        #
## Set up the test cases and solve them
import sys
#test_cases = open('spiralPrintingInput.txt','r')
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == '\n':
        continue
    test=test.strip()
    opt = test.split(';')
#    print opt
    data =[s for s in opt[2].split()]
#    print numbers
    rows = int(opt[0])
    cols = int(opt[1])
    # create the table
    table = []
    cur = 0
    for i in range(rows):
        elem = []
        for j in range(cols):
            elem.append(data[cur])
            cur+=1
        table.append(elem)
#    print table
    visited = [[False]*cols for x in xrange(rows)]
#    print visited
    spiralPrint(table,visited,(0,0),rows,cols)
    print

test_cases.close()



