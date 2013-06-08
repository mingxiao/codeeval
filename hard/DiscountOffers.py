'''
Created on Jul 15, 2012

@author: mingxiao10016
'''

import math
import string
"""
1. If the number of letters in the product's name is even then the SS is the number of 
vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5.
2. If the number of letters in the product's name is odd then the SS is the number of 
consonants in the customer's name.
3. If the number of letters in the product's name shares any common factors (besides 1) 
with the number of letters in the customer's name then the SS is multiplied by 1.5.

Apply rule 3 after determining whether rule 1 or 2 applies
"""
vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']

def score(product, customer):
    score = 0
    p_letters = len([c for c in product if c in string.ascii_letters])
    c_letters = len([c for c in customer if c in string.ascii_letters])
    if p_letters%2 == 0:
        num_vowels = len([c for c in customer if c in vowels])
        score = num_vowels*1.5
    else:
        score = len([c for c in customer if c not in vowels and c in string.ascii_letters])
    #now check if rule 3 applies
    if gcd(p_letters,c_letters) > 1:
        score *= 1.5
    return score    
    
def gcd(a,b):
    if b == 0:
        return a
    else: 
        return gcd(b,a%b)

def parse_input(testcase):
    cust = testcase.split(';')[0]
    prods = testcase.split(';')[1]
    cust = cust.split(',')
    prods = prods.split(',')
    assert len(cust) >0
    assert len(prods)>0
    return cust,prods

class Edge():
    def __init__(self,u,v,w):
        self.source = u
        self.sink = v
        self.capacity = w
        self.weight=w
    
    def __repr__(self):
        return '{}-->{}:{}'.format(self.source,self.sink,self.weight)

class BipartiteGraph():
    def __init__(self):
        self.L = []
        self.R = []
        self.adg={}
        self.edges = []
        
    def add_Lvertex(self,v):
        self.L.append(v)
        self.adg[v] = []
        
    def add_Rvertex(self,v):
        self.R.append(v)
        self.adg[v]=[]
        
    def add_edge(self,u,v,w):
        assert u in self.L
        assert v in self.R
        e = Edge(u,v,w)
        self.edges.append(e)
        self.adg[u].append(e)
        self.adg[v].append(e)
        
    def __repr__(self):
        r = ""
        for s in self.L:
            for e in self.adg[s]:
                r = r + repr(e) +'\n'
        return r
    
    def _max_weight(self,v):
        return max([e.weight for e in self.adg[v]])
    
    def _min_weight(self,v):
        return min([e.weight for e in self.adg[v]])
    
    def reduce_min(self):
        for v in self.L:
            m = self._min_weight(v)
            for k in self.adg[v]:
                k.weight = k.weight -m
                
    def subgraph0(self):
        fn = FlowNetwork()
        fn.add_vertex('s')
        fn.add_vertex('t')
        for e in self.edges:
            if e.weight == 0:
                source = e.source
                sink = e.sink
                fn.add_vertex(source)
                fn.add_vertex(sink)
                fn.add_edge(source,sink,1)
                fn.add_edge('s', source, 1)
                fn.add_edge(sink, 't', 1)
        print fn.max_flow('s','t')
    
    
class FlowNetwork(object):
    def __init__(self):
        self.V = []
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
        if vertex not in self.V:
            self.adj[vertex] = []
 
    def get_edges(self, v):
        return self.adj[v]
 
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge,residual) in path:
                result = self.find_path( edge.sink, sink, path + [(edge,residual)] )
                if result != None:
                    return result
 
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            flow = min(res for edge,res in path)
            for edge,res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))

