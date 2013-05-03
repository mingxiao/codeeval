import unittest
import ReverseAndAdd as ra

class Test(unittest.TestCase):

    def test_palindrome(self):
        s = '111'
        s2 = '121'
        s3= '13844'
        self.assertTrue(ra.palindrome(s))
        self.assertTrue(ra.palindrome(s2))
        self.assertFalse(ra.palindrome(s3))

    def test_process(self):
        n = 195
        self.assertEqual( ra.process(195), (4,9339))

if __name__ == '__main__':
    unittest.main()
