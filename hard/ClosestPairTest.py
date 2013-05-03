'''
Created on Jul 17, 2012

@author: mingxiao10016
'''
import unittest
import ClosestPair

class Test(unittest.TestCase):


    def testDist(self):
        print ClosestPair.dist((1,1), (4,5))
        l = [(0,2),(6,67),(43,71),(39,107),(189,140)]
        print ClosestPair.closestPair(l)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()