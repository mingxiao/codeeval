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
    
class Graph:
    def __init__(self, g):
        self.g = g
    def V(self):
        return self.g.keys()
    def Adj(self,v):
        return self.g[v].keys()
    def w(self,u,v):
        return self.g[u][v]
    def insert(self,u,v):
        scr = score(u,v)
        if u in self.V():
            self.g[u][v]=scr
            pass
        else:
            self.g[u]={v:scr}
    def toString(self):
        return self.g




