import unittest
import Email as em

class Test(unittest.TestCase):
    def test_valid(self):
        s = 'foo@bar.com'
        self.assertTrue(em.valid(s))
        s1 = 'admin#codeeval.com'
        self.assertFalse(em.valid(s1))
        s2 = 'good123@bad.com'
        self.assertTrue(em.valid(s2))

        t1 = 'g@h@j.com'
        self.assertFalse(em.valid(t1))

    
if __name__=='__main__':
    unittest.main()
