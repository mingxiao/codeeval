'''
Created on May 4, 2013

@author: mingxiao10016
'''
import unittest
import MatrixDiscountOffers as mdf


class Test(unittest.TestCase):

    def setUp(self):
        t = 'Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow'
        c,p = mdf.parse_input(t)
        self.m = mdf.form_matrix(c,p)
        t2 = 'Jeffery Lebowski,Walter Sobchak,Theodore Donald Kerabatsos,Peter Gibbons,Michael Bolton,Samir Nagheenanajar;Half & Half,Colt M1911A1,16lb bowling ball,Red Swingline Stapler,Printer paper,Vibe Magazine Subscriptions - 40 pack'
        c2,p2 = mdf.parse_input(t2)
        self.m2 = mdf.form_matrix(c2,p2)
        t3 = 'Jareau Wade,Rob Eroh,Mahmoud Abdelkader,Wenyi Cai,Justin Van Winkle,Gabriel Sinkin,Aaron Adelson;Batman No. 1,Football - Official Size,Bass Amplifying Headphones,Elephant food - 1024 lbs,Three Wolf One Moon T-shirt,Dom Perignon 2000 Vintage'
        c3,p3 = mdf.parse_input(t3)
        self.m3 = mdf.form_matrix(c3,p3)
    
    def test_form_matrix(self):
        print self.m3
#     def test_reduce_col(self):
#         #mdf.reduce_col(self.m)
#         pass

#     def test_ccover(self):
#         print self.m
#         mp = mdf.reduce_row(self.m)
#         print mp
#         print mdf.ccovered(mp, 2)
        
#     def test_rcover(self):
#         pass
# #        print mdf.rcovered(mp, 2)

    def test_hungarian(self):
        print self.m
        coors = mdf.hungarian(self.m)
        r =mdf.ans(self.m,coors)
        print r

        c2 = mdf.hungarian(self.m2)
        r2 = mdf.ans(self.m2,c2)
        print r2
        
        c3 = mdf.hungarian(self.m3)
        r3 = mdf.ans(self.m3,c3)
        print r3

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
