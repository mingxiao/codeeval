from copy import deepcopy
count = 0

def func(a):
    c = copy(a)
    c[2]=True

def move(x,y,visited,xmax,ymax):
    global count
    visited[x][y] = True
    #print x,y,visited
    if x == xmax and y == ymax:
        count += 1
        return
    #move right
    if y+1 <= ymax and visited[x][y+1] is False:
        move(x,y+1,deepcopy(visited),xmax,ymax)
    #move left
    if y-1 >=0 and visited[x][y-1] is False:
        move(x,y-1,deepcopy(visited),xmax,ymax)
    #move down
    if x+1 <=xmax and visited[x+1][y] is False:
        move(x+1,y,deepcopy(visited),xmax,ymax)
    #move up
    if x-1 >=0 and visited[x-1][y] is False:
        move(x-1,y,deepcopy(visited),xmax,ymax)

def form_visited(n):
    v = []
    for i in range(n):
        h = []
        for j in range(n):
            h.append(False)
        v.append(h)
    return v
n=4
been = form_visited(n)
move(0,0,been,n-1,n-1)
print count
