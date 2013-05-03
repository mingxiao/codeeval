'''
Created on Jul 15, 2012

@author: mingxiao10016
'''
import unittest
import DiscountOffers
from DiscountOffers import Graph

class Test(unittest.TestCase):


    def testGCD(self):
        self.assertEqual(DiscountOffers.gcd(10, 5),5)
        self.assertEqual(DiscountOffers.gcd(20, 3),1)
#        print DiscountOffers.score("Nerf Crossbow", "Ted Dziuba")
        
    def testCreateGraph(self):
        input = "Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow"
        print DiscountOffers.create_graph(input)
        
    def testGraph(self):
        graph = Graph({})
        graph.insert("iPad 2 - 4-pack","Jack Abraham")
        print graph.toString()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()