'''
Created on Jul 13, 2012

@author: mingxiao10016
'''
import unittest
import UglyNumbers
import timeit


class Test(unittest.TestCase):


    def testIsUgly(self):
        assert UglyNumbers.isUgly(236)
        assert UglyNumbers.isUgly(14)
        self.assertFalse(UglyNumbers.isUgly(13))
        
    def testFuncDriver(self):
        pass
#        UglyNumbers.func_driver("011")
    
    def testCountUglie(self):
        pass
        self.assertEqual(UglyNumbers.countUglie(['2','3','5','7']),4)
    
#    def testHash(self):
#        s = "123456"
#        half = len(s)/2
#        print s[:half]
#        print s[half:]
#        print type(eval("1-3"))
    
    def testPart(self):
        s='1234'
        uglist=UglyNumbers.part(s)
#        print UglyNumbers.lookUp
        print UglyNumbers.countUglie(uglist)
#        print '============'
#        UglyNumbers.func_driver(s)
#        print UglyNumbers.countUglie(UglyNumbers.part("011"))
#        UglyNumbers.func_driver(s)
#        print UglyNumbers.lookUp

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testIsUgly']
    unittest.main()