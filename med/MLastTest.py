import unittest
import MLast as ml

class Test(unittest.TestCase):
    def test_mlast(self):
        l = ['a','b','c','d']
        i = 4
        self.assertEqual( ml.mlast(l,i),'a')
        self.assertEqual( ml.mlast(l,2),'c')
        pass

if __name__=='__main__':
    unittest.main()
