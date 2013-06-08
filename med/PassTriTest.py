import unittest
import PassTri as pt

class Test(unittest.TestCase):
    def test_tolist(self):
        s = '1 2 3 4 5'
        self.assertEqual(pt.tolist(s),[1,2,3,4,5])

    def test_next(self):
        p0 = []
        cur = [5]
        print pt.next(p0,cur)
        p = [14,11]
        cur = [4,6,8]
        p2 = pt.next(p,cur)
        cur2 = [0,7,1,5]
        print pt.next(p2,cur2)
    pass

if __name__=='__main__':
    unittest.main()
