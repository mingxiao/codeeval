import unittest
import DoubleSquares as ds

class Test(unittest.TestCase):
    def test_double_squares(self):
        self.assertEqual(1,ds.num_double_squares(10))
        self.assertEqual(2,ds.num_double_squares(25))
        print ds.num_double_squares(2147483647)

if __name__=='__main__':
    unittest.main()
