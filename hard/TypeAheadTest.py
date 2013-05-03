'''
Created on Jul 14, 2012

@author: mingxiao10016
'''
import unittest
from TypeAhead import Bigram
import TypeAhead
from TypeAhead import Trigram

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

#    def testTrigram(self):
#        tg = Trigram()
#        print tg.table
#        tg.insert("hello", "how", "are")
#        tg.insert("hello", "there", "sir")
#        tg.insert("hello", "how", "many")
#        tg.insert("hello", "how", "many")
#        tg.insertLine("Mary had a little lamb its fleece was white as snow;")
#        print tg.table
#        print tg.print_ahead(tg.look_ahead("hello", "how"))

    def testBigram(self):
        bg = Bigram()
        for line in TypeAhead.lines:
            bg.insertLine(line)
#        print bg.table
        slist = bg.look_ahead('the')
        print bg.print_2(slist)
        self.assertEqual(bg.print_2(slist),"lamb,0.375;teacher,0.250;children,0.125;eager,0.125;rule,0.125")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()