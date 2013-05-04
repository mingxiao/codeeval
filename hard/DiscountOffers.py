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

def solve(cust,prods):
    g = FlowNetwork()
    g.add_vertex('s')
    g.add_vertex('t')
    map(g.add_vertex,cust)
    map(g.add_vertex,prods)
    #add source and sink
    MAX = 10000000
    for c in cust:
        g.add_edge('s',c,MAX)
    for p in prods:
        g.add_edge(p,'t',MAX)
    #add edges
    for c in cust:
        for p in prods:
            s = score(p,c)
            g.add_edge(c,p,s)
            assert s > 0
            print '{} -->{}: {}'.format(c,p,s)
    #solve
    print g.max_flow('s','t')
    pass
    
class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)
 
class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
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



