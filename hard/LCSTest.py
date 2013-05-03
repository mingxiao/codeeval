'''
Created on Jul 15, 2012

@author: mingxiao10016
'''
import unittest
import LCS

class Test(unittest.TestCase):
    
    def testLCS(self):
        s1 = "abc"
        s2 = "dabc"
        t1 = 'XMJYAUZ'
        t2 = 'MZJAWXU'
        t = LCS.lcs(t1,t2)
        print t
        self.assertEqual(t, "MJAU")
#        for row in t:
#            print row
#        print LCS.print_LCS(t, t1, t2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()