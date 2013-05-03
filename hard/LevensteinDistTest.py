'''
Created on Jul 18, 2012

@author: mingxiao10016
'''
import unittest
from LevensteinDist import TrieNode


class Test(unittest.TestCase):


    def testTrie(self):
        t = TrieNode()
        t.insert("hello")
        t.insert("help")
        t.printTrie()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testTrie']
    unittest.main()