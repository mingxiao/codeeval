import unittest
import MinPathSum as mps

class Test(unittest.TestCase):

    def test_solve(self):
        m = [[4,6],[2,8]]
        print mps.solve(m)

    def test_form_matrix(self):
        t = ['4,6','2,8']
        mps.form_matrix(t)
    pass

if __name__ == '__main__':
    unittest.main()
