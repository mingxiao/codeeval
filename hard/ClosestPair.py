'''
Created on Jul 17, 2012

@author: mingxiao10016
'''
import sys
import math
# euclidean dist between two points (x,y)
def dist(p1,p2):
    a = abs(p1[0]-p2[0])
    b = abs(p1[1]-p2[1])
#    print a,b
    return math.sqrt( math.pow(a,2) + math.pow(b,2))

#given a list points (x,y) sorted on the x axis, returns the distance between
# the closest pair of points
# list in form [(x1,y1),...,(xn,yn)]
def closestPair(pList):
    if len(pList) ==2:
        # base case, only 2 points so they are by definition the closest pair
        return dist(pList[0],pList[1])
    elif len(pList) == 3:
        return min(dist(pList[0],pList[1]), dist(pList[0],pList[2]), dist(pList[1],pList[2]))
    else:
        mid = len(pList)/2
        # minimum pair among the left and right path
        left = pList[:mid]
        right = pList[mid:]
#        print left,right
        Lmin = closestPair(left)
        Rmin = closestPair(right)
        LRmin = sys.maxint
        for l in left:
            for r in right:
                d = dist(l,r)
                if d < LRmin:
                    LRmin =d
    return min(Lmin,Rmin,LRmin)

test_cases = open(sys.argv[1],'r')
#test_cases = open("closestPairInput.txt",'r')
test = test_cases.readline().strip()
while test != '0':
#    print test
    points = []
    for i in range(int(test)):
        tmp = test_cases.readline().strip()
        point = tmp.split()
        point_tup = (int(point[0]),int(point[1]))
#        print 'tmp',tmp,point, point_tup
        points.append(point_tup)
#    print points
    d = closestPair(points)
    if d >= 10000:
        print "INFINITY"
    else:
        print "%.4f" %d
    test = test_cases.readline().strip()

test_cases.close()




