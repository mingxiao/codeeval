'''
Created on Jul 12, 2012

@author: mingxiao10016
'''
import unittest
import TextDollar

class Test(unittest.TestCase):


    def testSpellOne(self):
        self.assertEqual(TextDollar.spellOneDigit("1"),"One")
        self.assertEqual(TextDollar.spellOneDigit("2"),"Two")
        self.assertEqual(TextDollar.spellOneDigit("3"),"Three")
        
    def testSpellTwo(self):
        self.assertEqual(TextDollar.spellTwoDigit("12"),"Twelve")
        self.assertEqual(TextDollar.spellTwoDigit("11"),"Eleven")
        self.assertEqual(TextDollar.spellTwoDigit("10"),"Ten")
        self.assertEqual(TextDollar.spellTwoDigit("80"),"Eighty")
        self.assertEqual(TextDollar.spellTwoDigit("91"),"NinetyOne")
        self.assertEqual(TextDollar.spellTwoDigit("01"),"One")
        
    def testSpellThree(self):
        self.assertEqual(TextDollar.spellThreeDigit("100"),"OneHundred")
        self.assertEqual(TextDollar.spellThreeDigit("129"),"OneHundredTwentyNine")
        self.assertEqual(TextDollar.spellThreeDigit("044"),"FortyFour")
        self.assertEqual(TextDollar.spellThreeDigit("999"),"NineHundredNinetyNine")
        self.assertEqual(TextDollar.spellThreeDigit("000"),"")
        
    def testSplitIntoThrees(self):
        self.assertEqual(TextDollar.splitIntoThrees("12345"),['345', '12'])
        self.assertEqual(TextDollar.splitIntoThrees("100000"),['000', '100'])
        pass
    
    def testSpellGroup(self):
        print TextDollar.spellGroups(['345','12'])
        print TextDollar.spellGroups(['3'])
        print TextDollar.spellGroups(['466'])
        pass
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpellOne']
    unittest.main()