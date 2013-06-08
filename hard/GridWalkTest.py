import unittest
import GridWalk as gw

class Test(unittest.TestCase):
    def test_score(self):
        self.assertEqual(gw.score(59,79),30)
        self.assertEqual(gw.score(-5,-7),12)
        self.assertEqual(gw.score(298,0),19)

    def test_dpwalk(self):
        print gw.dpwalk(19)

if __name__== '__main__':
    unittest.main()
