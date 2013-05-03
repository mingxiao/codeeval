'''
Created on Jul 15, 2012

@author: mingxiao10016
'''
import unittest
import StringPermute


class Test(unittest.TestCase):


    def testEnum(self):
        s='hello'
        for i,c in enumerate(s):
            print i,c
            
    def testPermute(self):
        s='hat'
        self.assertEqual(StringPermute.print_permute(s),"aht,ath,hat,hta,tah,tha")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()