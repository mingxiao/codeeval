'''
Created on Jul 15, 2012

@author: mingxiao10016
'''
import unittest
import DiscountOffers as df

class Test(unittest.TestCase):

    def test_score(self):
        self.assertEqual(df.gcd(10, 5),5)
        self.assertEqual(df.gcd(20, 3),1)
        self.assertEqual( df.score("Nerf Crossbow", "Ted Dziuba"),9)

    def test_FlowNetwork(self):
        g = df.FlowNetwork()
        map(g.add_vertex,['s','a','b','t'])
        g.add_edge('s','a',24.534)
        g.add_edge('a','t',10.5)
        g.add_edge('s','b',10)
        g.add_edge('a','b',30)
        g.add_edge('b','t',20)
        print g.max_flow('s','t')

    def test_parse_input(self):
        t = 'Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow'
        c,p = df.parse_input(t)
        print c,p
        df.solve(c,p)

        t2 = 'Jeffery Lebowski,Walter Sobchak,Theodore Donald Kerabatsos,Peter Gibbons,Michael Bolton,Samir Nagheenanajar;Half & Half,Colt M1911A1,16lb bowling ball,Red Swingline Stapler,Printer paper,Vibe Magazine Subscriptions - 40 pack'
        c2,p2 = df.parse_input(t2)
        df.solve(c2,p2)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
