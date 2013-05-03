'''
Created on Jul 18, 2012

@author: mingxiao10016
'''

# A trie for words in our list. 
class TrieNode():
    def __init__(self):
        self.word = None # will be non-None if it is a valid word in our list
        self.children = {}
    
    def insert(self,word):
        curNode = self
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.word = word
    
    
    # prints the Trie, for debugging purposes.
    # if we inserted the words "hello" and "help" then the Trie looks like
# h
#    e
#        l
#            p
#            l
#                o
    def printTrie(self):
        self.printRecursive(self,0)
    
    def printRecursive(self,node,numTabs):
        for letter,child in node.children.items():
            print '\t' * numTabs,letter
            self.printRecursive(child,numTabs+1)
            
import sys
import time
trie = TrieNode()
words = open("wordList.txt",'r')
for word in words:
#    print word.strip()
    trie.insert(word.strip())
    
# The search function returns a list of all words that are less than the given
# maximum distance from the target word
def search( word, maxCost ):

    # build first row
    currentRow = range( len(word) + 1 )
#    print currentRow
    results = []

    # recursively search each branch of the trie
    for letter in trie.children:
#        print letter,word
        searchRecursive( trie.children[letter], letter, word, currentRow, 
            results, maxCost )

    return results

# This recursive helper is used by the search function above. It assumes that
# the previousRow has been filled in already.
def searchRecursive( node, letter, word, previousRow, results, maxCost ):
#    print node,letter,word,previousRow,results
    columns = len( word ) + 1
    currentRow = [ previousRow[0] + 1 ]
#    print previousRow, currentRow
    # Build one row for the letter, with a column for each letter in the target
    # word, plus one for the empty string at column 0
    for column in xrange( 1, columns ):

        insertCost = currentRow[column - 1] + 1
        deleteCost = previousRow[column] + 1

        if word[column - 1] != letter:
            replaceCost = previousRow[ column - 1 ] + 1
        else:                
            replaceCost = previousRow[ column - 1 ]

        currentRow.append( min( insertCost, deleteCost, replaceCost ) )
#        print insertCost,deleteCost,replaceCost,currentRow

    # if the last entry in the row indicates the optimal cost is less than the
    # maximum cost, and there is a word in this trie node, then add it.
    if currentRow[-1] <= maxCost and node.word != None:
        results.append( node.word )

    # if any entries in the row are less than the maximum cost, then 
    # recursively search each branch of the trie
    if min( currentRow ) <= maxCost:
        for letter in node.children:
            searchRecursive( node.children[letter], letter, word, currentRow, 
                results, maxCost )

#keeps track of the words we've seen. only interested in the key, not the value
#used a dictionary instead of a list for speed
graph={} 

# recursive definition does not work due to python's recursion depth limit
# need iterative solution
#def network(word):
#    if word not in graph:
#        graph[word]=1
#        result = search(word,1)
##        print word,result
#        for r in result:
#            network(r,)
start = time.time()
word = 'abcde'
#graph[word]=1
q = search(word,1)
print q
while q:
    word = q.pop()
    if word not in graph:
        graph[word]=1
        r = search(word,1)
        q += r
end = time.time()
print "Graph creation took %g s" % (end - start)
#print graph
print len(graph)

# the current solution takes TOO Long ~20s