import unittest
import SimpleCalculator as sc

class CalcTest(unittest.TestCase):
    def test_get_tokens(self):
        s1 = '250*14.3'
#        print sc.get_tokens(s1)
        s2 = '3^6 / 117'
#        print sc.get_tokens(s2)
        s3 = '(2.16 - 48.34)^-1'
#        print sc.get_tokens(s3)
        s4 = '(59 - 15 + 3*6)/21'
#        print sc.get_tokens(s4)
    
    def test_shunting_yard(self):
        s1 = '250*14.3'
        t1 = sc.get_tokens(s1)
        #sc.shunting_yard(t1)
    
    def test_prec(self):
        self.assertTrue(sc.prec('*','/'))
        self.assertTrue(sc.prec('*','-'))

    def test_shunting_yard(self):
        instr = '3 + 4'
        tokens = sc.get_tokens(instr)
        ans = ['3', '4', '+']
        rpn = sc.shunting_yard(tokens)
        self.assertEqual(ans,rpn)
        self.assertEqual(7,sc.eval_rpn(rpn))

        instr = '3 - 4'
        tokens = sc.get_tokens(instr)
        ans = ['3', '4', '-']
        rpn = sc.shunting_yard(tokens)
        self.assertEqual(ans,rpn)
        self.assertEqual(-1,sc.eval_rpn(rpn))
        
        instr2 = '3^6 / 117'
        tok2 = sc.get_tokens(instr2)
        ans2 = ['3','6','^','117','/']
        rpn2 = sc.shunting_yard(tok2)
        self.assertEqual(ans2,rpn2)
        self.assertEqual(6.23 ,round(sc.eval_rpn(rpn2),2))

        instr2a = '(3+1)'
        tok2a = sc.get_tokens(instr2a)
        ans2a = ['3','1','+']
        rpn2a = sc.shunting_yard(tok2a)
        self.assertEqual(ans2a,rpn2a)
        self.assertEqual(4,sc.eval_rpn(rpn2a))

        instr3 = '(3+22) ^ 4'
        tok3 = sc.get_tokens(instr3)
        ans3 = ['3','22','+','4','^']
        rpn3 = sc.shunting_yard(tok3)
        self.assertEqual(ans3,rpn3)
        self.assertEqual(390625,sc.eval_rpn(rpn3))

    def test_truncate_float(self):
        f = 16.00
        print sc.truncate_float(f)
    

if __name__ == '__main__':
    unittest.main()
