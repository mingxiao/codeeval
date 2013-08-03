import unittest
import CommutingEngineer as ce
from sets import Set
import pprint

class Test(unittest.TestCase):
    def test_dist(self):
        print ce.dist(1,4,2,7)
        print ce.dist(37.7768016,-122.4169151,37.7860105,122.4025377)

    def test_to_bitstr(self):
        self.assertEqual('010010',ce.to_bitstr(6,[1,4]))
        self.assertEqual('111',ce.to_bitstr(3,Set((0,1,2))))

    def test_k_subsets(self):
        for x in ce.k_subsets([1,2,3],2):
            pass

    def test_form_dists(self):
        c = [(1,0),(2,3),(-1,-1)]
        d = ce.form_dists(c)
        end,scost,route = ce.TSP(d)
#        print end, scost,route

    def test_print_route(self):
        r = {'100': {0: ('100', 0)}, '101': {2: ('100', 0)}, '111': {1: ('101', 2), 2: ('110', 1)}, '110': {1: ('100', 0)}}
        S = '111'
        end = 1
        ce.print_route(r,S,end)

    def test_get_coors(self):
        line = '1 | CodeEval 1355 Market St, SF (37.7, -122.4)'
        self.assertEqual((37.7,-122.4),ce.get_coors(line))
        
    def test_file_to_coors(self):
        f = 'CommutingEngineerInput.txt'
        locations = ce.file_to_coors(f)
        dists = ce.form_dists(locations)
        pprint.pprint(dists)
        end,scost,route = ce.TSP(dists)
        print end
        print scost
        print route
        S = '1'*len(locations)
        ce.print_route(route,S,end)

if __name__=='__main__':
    unittest.main()
