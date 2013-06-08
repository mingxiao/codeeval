import unittest
import RobotMove as rm

class Test(unittest.TestCase):
    def test_func(self):
        t = [False] * 4
        print t
        rm.func(t)

    def test_form_visited(self):
        g = rm.form_visited(4)
        print g
        g[2][2] = True
        print g
    pass

if __name__ == '__main__':
    unittest.main()
