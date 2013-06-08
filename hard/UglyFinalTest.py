import unittest
import UglyNumberFinal as ugly

class Test(unittest.TestCase):
    def test_permute(self):
        s= '123'
        ops = ['','+','-']
        ugly.permute(s,ops)
    pass

if __name__ == '__main__':
    unittest.main()
