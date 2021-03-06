import unittest
import DaVyncy as dv

class Test(unittest.TestCase):
    def setUp(self):
        self.test1= 'O draconia;conian devil! Oh la;h lame sa;saint!' 
        self.test2 = 'm quaerat voluptatem.;pora incidunt ut labore et d;, consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;uptatem.;i dolorem ipsum qu;iquam quaerat vol;psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;dipisci velit, sed quia non numqua;us modi tempora incid;Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al'
        self.test3 = s3 = 'WHMHT_p\fDZsJo;FjhEzTAYPdDEEqaB;XmgfCrBwqYfy^qlsGvs;jvjSxwcusgKqsgyjTZ;xGSJzmwq[jO[oPYdTxMW;ONW\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXm;gfCrBwqYfy^qlsGvsjv;jSxwcusgKqsgyjTZxG;SJzmwq[jO[oPYdTxMWO;NW\zUKsSnTgI;WHMHT_p\f;DZsJo;FjhEzTAYPdDEEqaB;XmgfCrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjT;ZxGSJzmwq[jO[oP;YdTxMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTAYP;dDEEqaBXmgfCrBwqYfy;^qlsGvsjvjS;xwcusgKqsgyj;TZxGSJzmwq;[jO[oPYdTxMWONW\z;UKsSnTgI;WHMHT_p\fDZsJoFjhEzT;AYPdDEEqaBXmgfCrBw;qYfy^qlsGvsjvjS;xwcus;gKqsgyjTZxGSJ;zmwq[jO[o;PYdTxMWONW\zUKsS;nTgI;WHMHT_p\fDZsJ;oFjhEzTAYPdDEEqaBXmgfC;rBwqYfy^qls;GvsjvjSxwcusgKqsg;yjTZxGSJzmwq[jO[oPYd;TxMWONW\zUKs;SnTgI;WHMHT_p\fDZs;JoFjhEzTAYPdDEEqaBXmgfC;rBwq;Yfy^qlsGvsjvjSx;wcusgKqsgyjTZxGSJzm;wq[jO[oPYdTxMWONW;\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXmgfCr;BwqYfy^qlsGvsjvj;SxwcusgKqsgyjTZxGSJzmw;q[jO[oPYdT;xMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhE;zTAYPdDEEqa;BXmgfCrBwq;Yfy^qlsGvsjvjSx;wcusgKqsgyjTZxGSJzmwq;[jO[oPYdTxMWON;W\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTAY;PdDEEqaBXmgfCrBwqYf;y^qlsGvsjvjSxw;cusgKqsgyjTZxGSJzmwq[jO[o;PYdTxMWONW;\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTA;YPdDEEqaBXmgfCr;BwqYfy^qlsGvsjv;jSxwcusgKqsgyjTZx;GSJzmwq[jO[oPYd;TxMWONW\zUKsSnTgI;WHMHT_p\fDZs;JoFjhEzTAYPdDEE;qaBXmgfCrBwqYfy;^qlsGvsjvjSxwcu;sgKqsgyjTZxGSJzmwq[j;O[oPY;dTxMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhEz;TAYPdDEEqaBXmgfCrBwq;Yfy^ql;sGvsjvjSxwcusgKqsgyjTZxGS;Jzmwq[jO[oPYdTx;MWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXmg;fCrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjTZ;xGSJzmwq[jO[oPY;dTxMWONW\zU;KsSnTgI;WHMHT_p\fDZsJoFjhEzTA;YPdDEEqaBXmgf;CrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjTZxG;SJzmwq[jO[oPY;dTxMWONW\zUKsSnTgI'


    def test_allindices(self):
        sub = '\fDZ'
        str = 'WHMHT_p\fDZsJo'
        ans =  dv.allindices(str,sub)
        self.assertEqual([7],ans)

        s2 = 'abcdecd'
        sub2 = 'cd'
        ans2 = dv.allindices(s2,sub2)
        print ans2
        self.assertEqual([2,5],ans2)

    def test_finall_idx(self):
#         s1 = 'O draconia'
#         s2 = 'conia'
#         self.assertEqual(dv.findall_idx(s1,s2),[5])

        pat = '\fDZ'
        s = 'WHMHT_p\fDZsJo'
        ans = dv.findall_idx(s,pat)
        self.assertEqual(ans,[7])

    def test_overlap(self):
        s1 = 'abcdcd'
        s2 = 'cdefg'
        self.assertEqual(dv.overlap(s1,s2), 2)

        t1 = 'h lame sai'
        t2 = 'saint!'
        self.assertEqual(dv.overlap(t1,t2),3)

        r1 = 'abc\fDZsJo'
        r2 = '\fDZsJo123'
        ans= dv.overlap(r1,r2)
        self.assertEqual(6,ans)

    def test_reaches_end(self):
        s1 = 'abcdcd'
        s2 = 'cdefg'
        pos = 4
        self.assertTrue(dv.reaches_end(s1,s2,pos))
        self.assertFalse(dv.reaches_end(s1,s2,3))

        s3 = 'O draconia'
        s4 = 'conian devil!'
        self.assertTrue(dv.reaches_end(s3,s4,5))

        s5 = '12345'
        s6 = '34678'
        self.assertFalse(dv.reaches_end(s5,s6,2))

        s7 = 'WHMHT_p\fDZsJo'
        s8 = '\fDZsJo123'
        self.assertTrue(dv.reaches_end(s7,s8,7))

    def test_split_input(self):
        s = 'O draconia;conian devil! Oh la;h lame sa;saint!'
        ans = ['O draconia','conian devil! Oh la','h lame sa','saint!']
        self.assertEqual(dv.split_input(s),ans)
        
       # print dv.split_input(self.test3)
        

    def test_combine(self):
        s1 = 'h lame sa'
        s2 = 'saint!'
        self.assertEqual(dv.combine(s1,s2,2),'h lame saint!')
        
        s3 = 'O draconia'
        s4 = 'conian devil!'
        self.assertEqual(dv.combine(s3,s4,5),'O draconian devil!')

    def test_max_item(self):
        d = {'a':1, ('c','d'):10}
        truth  = (('c','d'),10)
        ans = dv.max_item(d)
        self.assertEqual(truth, ans)

    def test_solve(self):
#        s = 'O draconia;conian devil! Oh la;h lame sa;saint!'
#        ans = 'O draconian devil! Oh lame saint!'
#        self.assertEqual( dv.solve(s), ans)

#        s2='m quaerat voluptatem.;pora incidunt ut labore et d;, consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;uptatem.;i dolorem ipsum qu;iquam quaerat vol;psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;dipisci velit, sed quia non numqua;us modi tempora incid;Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al'
#        ans2 = 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.'
#        self.assertEqual(dv.solve(s2),ans2)

        s3 = r'WHMHT_p\fDZsJo;FjhEzTAYPdDEEqaB;XmgfCrBwqYfy^qlsGvs;jvjSxwcusgKqsgyjTZ;xGSJzmwq[jO[oPYdTxMW;ONW\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXm;gfCrBwqYfy^qlsGvsjv;jSxwcusgKqsgyjTZxG;SJzmwq[jO[oPYdTxMWO;NW\zUKsSnTgI;WHMHT_p\f;DZsJo;FjhEzTAYPdDEEqaB;XmgfCrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjT;ZxGSJzmwq[jO[oP;YdTxMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTAYP;dDEEqaBXmgfCrBwqYfy;^qlsGvsjvjS;xwcusgKqsgyj;TZxGSJzmwq;[jO[oPYdTxMWONW\z;UKsSnTgI;WHMHT_p\fDZsJoFjhEzT;AYPdDEEqaBXmgfCrBw;qYfy^qlsGvsjvjS;xwcus;gKqsgyjTZxGSJ;zmwq[jO[o;PYdTxMWONW\zUKsS;nTgI;WHMHT_p\fDZsJ;oFjhEzTAYPdDEEqaBXmgfC;rBwqYfy^qls;GvsjvjSxwcusgKqsg;yjTZxGSJzmwq[jO[oPYd;TxMWONW\zUKs;SnTgI;WHMHT_p\fDZs;JoFjhEzTAYPdDEEqaBXmgfC;rBwq;Yfy^qlsGvsjvjSx;wcusgKqsgyjTZxGSJzm;wq[jO[oPYdTxMWONW;\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXmgfCr;BwqYfy^qlsGvsjvj;SxwcusgKqsgyjTZxGSJzmw;q[jO[oPYdT;xMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhE;zTAYPdDEEqa;BXmgfCrBwq;Yfy^qlsGvsjvjSx;wcusgKqsgyjTZxGSJzmwq;[jO[oPYdTxMWON;W\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTAY;PdDEEqaBXmgfCrBwqYf;y^qlsGvsjvjSxw;cusgKqsgyjTZxGSJzmwq[jO[o;PYdTxMWONW;\zUKsSnTgI;WHMHT_p\fDZsJoFjhEzTA;YPdDEEqaBXmgfCr;BwqYfy^qlsGvsjv;jSxwcusgKqsgyjTZx;GSJzmwq[jO[oPYd;TxMWONW\zUKsSnTgI;WHMHT_p\fDZs;JoFjhEzTAYPdDEE;qaBXmgfCrBwqYfy;^qlsGvsjvjSxwcu;sgKqsgyjTZxGSJzmwq[j;O[oPY;dTxMWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjhEz;TAYPdDEEqaBXmgfCrBwq;Yfy^ql;sGvsjvjSxwcusgKqsgyjTZxGS;Jzmwq[jO[oPYdTx;MWONW\zUKsSnTgI;WHMHT_p\fDZsJoFjh;EzTAYPdDEEqaBXmg;fCrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjTZ;xGSJzmwq[jO[oPY;dTxMWONW\zU;KsSnTgI;WHMHT_p\fDZsJoFjhEzTA;YPdDEEqaBXmgf;CrBwqYfy^qlsG;vsjvjSxwcusgKqsgyjTZxG;SJzmwq[jO[oPY;dTxMWONW\zUKsSnTgI'
        ans = dv.solve(s3)
        print 'ANS'
        print ans
        for c in ans:
            if c == '\f':
                print 'slash f encountered'

if __name__ == '__main__':
    unittest.main()
