'''
Created on Jul 18, 2012

@author: mingxiao10016
'''
import unittest
import SpiralPrinting

class Test(unittest.TestCase):

    def setUp(self):
        self.table = [[1,2,3],
         [4,5,6],
         [7,8,9]]
        self.visited = [[False]*3 for x in xrange(3)]

    def testCanPrintRight(self):
        pass
#        print self.table
#        print SpiralPrinting.canPrintRight(self.visited, (0,0), 3, 3)
#        print SpiralPrinting.canPrintRight(self.visited, (2,1), 3, 3)
##        self.visited[0][2]=True
#        print SpiralPrinting.printRight(self.visited, (0,0), 3, 3)
#        print SpiralPrinting.printRight(self.visited, (1,0), 3, 3)
        
    def testCanPrintUp(self):
        print self.visited
        print SpiralPrinting.spiralPrint(self.table,self.visited, (0,0), 3, 3)
        print self.visited
        print 'here'
#        print SpiralPrinting.canPrintUp(self.visited, (0,0), 3, 3)
#        print self.table[0][0]
#        self.visited[0][0] = True
#        c = SpiralPrinting.printRight(self.visited, (0,0), 3, 3)
#        c = SpiralPrinting.printDown(self.visited, c, 3, 3)
#        c = SpiralPrinting.printLeft(self.visited, c, 3, 3)
#        c = SpiralPrinting.printUp(self.visited, c, 3, 3)
#        print self.visited
#        print SpiralPrinting.printLeft(self.visited, (0,2), 3, 3)
#        print SpiralPrinting.printUp(self.visited, (2,2), 3, 3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCanPrintRight']
    unittest.main()