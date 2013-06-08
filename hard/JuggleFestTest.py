import unittest
import JuggleFest as jf

class Test(unittest.TestCase):
    
    def test_dot(self):
        l1 = [1,2,3]
        l2 = [4,5,6]
        self.assertEqual(jf.dot(l1,l2),32)

    def test_form_list(self):
        h = "H:2"
        e = "E:9"
        p = "P:0"
        ans = [2,9,0]
        self.assertEqual(jf.form_list(h,e,p),ans)

    def test_circuits(self):
        lines = ['C C0 H:7 E:7 P:10\n',
                 'C C1 H:2 E:1 P:1\n']
#        print jf.form_dict(lines)

    def test_prefs(self):
        lines = ['J J0 H:3 E:9 P:2 C2,C0,C1\n',
                 'J J9 H:10 E:2 P:1 C1,C2,C0\n']
#        print jf.prefs(lines)

    def test_next_circuit(self):
        pref = ['C1','C2','C3']
        proposed =[]
        self.assertEqual(jf.next_circuit(pref,proposed),'C1')
        proposed = ['C1']
        self.assertEqual(jf.next_circuit(pref,proposed),'C2')

    def test_match(self):
        clines ="""C C0 H:7 E:7 P:10
C C1 H:2 E:1 P:1
C C2 H:7 E:6 P:4""".split('\n')
        jlines = """J J0 H:3 E:9 P:2 C2,C0,C1
J J1 H:4 E:3 P:7 C0,C2,C1
J J2 H:4 E:0 P:10 C0,C2,C1
J J3 H:10 E:3 P:8 C2,C0,C1
J J4 H:6 E:10 P:1 C0,C2,C1
J J5 H:6 E:7 P:7 C0,C2,C1
J J6 H:8 E:6 P:9 C2,C1,C0
J J7 H:7 E:1 P:5 C2,C1,C0
J J8 H:8 E:2 P:3 C1,C0,C2
J J9 H:10 E:2 P:1 C1,C2,C0
J J10 H:6 E:4 P:5 C0,C2,C1
J J11 H:8 E:4 P:7 C0,C1,C2""".split('\n')
        circuit = jf.form_dict(clines)
        jugglers = jf.form_dict(jlines)
        prefs = jf.prefs(jlines)
        print circuit
        print jugglers
        print prefs
        m = jf.match(circuit,jugglers,prefs)
        print m
        self.assertEqual(jf.ans(m,2),417)
        pass

    def test_better_match(self):
        clist = [('J9', 23), ('J8',9)]
        d = 10
        self.assertTrue(jf.better_match(clist,d))
        d = 1
        self.assertFalse(jf.better_match(clist,d))
        

    def test_worst(self):
        clist = [('J9', 23), ('J4',2)]
        self.assertEqual(jf.worst_member(clist),('J4',2))

if __name__ == '__main__':
    unittest.main()
    pass
