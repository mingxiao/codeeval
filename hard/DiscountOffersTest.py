'''
Created on Jul 15, 2012

@author: mingxiao10016
'''
import unittest
import DiscountOffers as df

class Test(unittest.TestCase):
    def setUp(self):
        self.g = df.BipartiteGraph()
        self.g.add_Lvertex('x1')
        self.g.add_Lvertex('x2')
        self.g.add_Lvertex('x3')
        self.g.add_Rvertex('y1')
        self.g.add_Rvertex('y2')
        self.g.add_Rvertex('y3')
        
        self.g.add_edge('x1', 'y1', 1)
        self.g.add_edge('x1', 'y2', 4)
        self.g.add_edge('x1', 'y3', 5)
        
        self.g.add_edge('x2', 'y1', 5)
        self.g.add_edge('x2', 'y2', 7)
        self.g.add_edge('x2', 'y3', 6)
        
        self.g.add_edge('x3', 'y1', 5)
        self.g.add_edge('x3', 'y2', 8)
        self.g.add_edge('x3', 'y3', 8)

    def test_score(self):
        self.assertEqual(df.gcd(10, 5),5)
        self.assertEqual(df.gcd(20, 3),1)
        self.assertEqual( df.score("Nerf Crossbow", "Ted Dziuba"),9)

    def test_parse_input(self):
        t = 'Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow'
        c,p = df.parse_input(t)
        #print df.form_matrix(c,p)
        
    def test_max_weight(self):
        self.assertEqual(self.g._max_weight('x1'),5)
        self.assertEqual(self.g._max_weight('x2'),7)
        
    def test_reduce_min(self):
        print self.g
        self.g.reduce_min()
        print self.g
        print self.g.adg['y1']
        self.g.subgraph0()

        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
