'''
Created on Jul 13, 2012

@author: mingxiao10016
'''
import unittest
import UglyNumbers
import timeit


class Test(unittest.TestCase):
    def test_permute(self):
        print UglyNumbers.allperms
        UglyNumbers.permdriver('0')
        print UglyNumbers.allperms
        print UglyNumbers.solve()
    def testIsUgly(self):
        assert UglyNumbers.isUgly(236)
        assert UglyNumbers.isUgly(14)
        self.assertFalse(UglyNumbers.isUgly(13))
        
    def testCountUglie(self):
        self.assertEqual(UglyNumbers.countUglie(['2','3','5','7']),4)
    
#    def testHash(self):
#        s = "123456"
#        half = len(s)/2
#        print s[:half]
#        print s[half:]
#        print type(eval("1-3"))
    
    def testPart(self):
        s='1234567890123'
        #uglist=UglyNumbers.part(s)
        #print UglyNumbers.countUglie(uglist)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testIsUgly']
    unittest.main()
