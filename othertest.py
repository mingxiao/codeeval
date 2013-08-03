import unittest
import otherugly as ugly

class Test(unittest.TestCase):
    def test_numop(self):
        instr = '943'
        opr = ugly.create_operations_array(len(instr)-1)
        print opr
        print ugly.get_number_operations(instr,opr[1],len(instr))
    pass


if __name__ == '__main__':
    unittest.main()
