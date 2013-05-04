import unittest
import StringSubstitution as ss

class Test(unittest.TestCase):
    def test_findall(self):
        s = 'abcdeabab'
        #print ss.findall(s,'ab')

    def test_available(self):
        u = [0,1,1,0,1]
        s = 3
        t = 4
        #self.assertTrue(ss.available(u,s,t))
    
    def test_replace_atidx(self):
        s = 'abcdefg'
        f = 'bc'
        r = '11'
        self.assertEqual( ss.replace_atidx(s,f,r,1),'a11defg')

    def test_redo_used(self):
        used = list('abcdefgh')
        s = 3
        flen = 2
        rlen = 4
        ss.redo_used(used,s,flen,rlen)

    def test_sub(self):
        s = '111010'
        used = [0]*6
        f = '10'
        r = '11'
##        s2, used2 = ss.sub(s,used,f,r)
##        print s2,used2
##        s3,used3 =  ss.sub(s2,used2,'11','000')
##        print s3, used3
##        print ss.sub(s3,used3,'0','10')

    def test_form(self):
        t = '10011011001;0110,1001,1001,0,10,11'
        #ss.form(t)

    def test_findfirst(self):
        s = 'abcdefabcde'
        f = 'cd'
        self.assertEqual( ss.findfirst(s,f,0),2)
        self.assertEqual( ss.findfirst(s,f,3),8)
        pass
    

    def test_sub2(self):
        s = '111010'
        used = [0]*6
        f = '10'
        r = '11'
##        s1,used1 = ss.sub2(s,used,f,r)
##        ss.sub2(s1,used1,'11','0010')

    def test_answer(self):
        t = '10011011001;0110,1001,1001,0,10,11'
        t2='10011010001011000111000111111110000010101011011011000101100010000111001;011001,1111,110,1011,1011,11'
        print ss.answer(t2)
        pass
        
    pass

if __name__ =='__main__':
    unittest.main()
