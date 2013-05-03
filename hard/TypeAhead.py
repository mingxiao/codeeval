'''
Created on Jul 14, 2012

@author: mingxiao10016
'''
import string
class Bigram():
    table ={} #table will be a hash of hashes (of string ==> int)
    def __init__(self):
        pass
    
    #inserts a line of input
    def insertLine(self,line):
        # remove punctuation
        exclude = set(string.punctuation)
        tokens = line.split(" ");
#        print tokens
        words = []
        for token in tokens:
            word = ''.join(ch for ch in token if ch not in exclude)
            words.append(word)
#        print words
        for i in range(len(words)-1):
            self.insert(words[i], words[i+1])
        
    
    def insert(self,str1,str2):
        if str1 in self.table:
            if str2 in self.table[str1]:
                self.table[str1][str2] = self.table[str1][str2] + 1
            else:
                self.table[str1][str2] = 1
        else:
            self.table[str1] = {str2:1}
    
    #returns a list of tuples containing (next_word,prob)
    def look_ahead(self,str1):
        result = []
        if str1 in self.table:
            str1_hash = self.table[str1]
            total = sum(str1_hash.values())
#            print float(total)
            for key in str1_hash.keys():
                prob = float(str1_hash[key])/total
#                print key,str1_hash[key], total,prob
                result.append((key,prob))
        return result
    
    #given a list of tuples (word,prob) prints the list in the correct order and format
    #need to sort alphabetically if they have same score
    # DO NOT USE, use print_2
    def print_ahead(self,ahead_list):
        ahead_list.sort(key=lambda x: x[1],reverse=True) #sort the list based on probability
#        print ahead_list
        for tup in ahead_list:
            if tup ==ahead_list[-1]:
                sys.stdout.write("%s,%.3f" %(tup[0],tup[1]))
#                print "%s,%.3f" %(tup[0],tup[1]),
            else:
                sys.stdout.write("%s,%.3f;" %(tup[0],tup[1]))
#                print "%s,%.3f;" %(tup[0],tup[1]),
        print
        
    def print_2(self,ahead_list):
        result = ''
        unique = sorted(set([x[1] for x in ahead_list]),reverse=True)
        for prob in unique:
            tmp = [tup[0] for tup in ahead_list if tup[1]==prob]
            tmp.sort()
#            print tmp
            for word in tmp:
                s = "%s,%.3f;" %(word,prob)
                result += s
        #remove the trialing semicolon
        return result[:-1]
        
    
    def ahead(self,word):
        l = self.look_ahead(word)
        print self.print_2(l)

class Trigram():
    table = {}
    def __init__(self):
        pass
    
    def insert(self,str1,str2,str3):
        if str1 in self.table:
            str1_hash = self.table[str1]
            if str2 in str1_hash:
                str2_hash = str1_hash[str2]
                if str3 in str2_hash:
                    str2_hash[str3] = str2_hash[str3]+1
                else:
                    str2_hash[str3]=1
            else:
                str1_hash[str2]={str3:1}
        else:
            self.table[str1]={str2:{str3:1}}
            
    def insertLine(self,line):
        # remove punctuation
        exclude = set(string.punctuation)
        tokens = line.split(" ");
#        print tokens
        words = []
        for token in tokens:
            word = ''.join(ch for ch in token if ch not in exclude)
            words.append(word)
#        print words
        for i in range(len(words)-2):
            self.insert(words[i], words[i+1],words[i+2])
    
    def look_ahead(self,str1,str2):
        result = []
        if str1 in self.table:
            str1_hash = self.table[str1]
            if str2 in str1_hash:
                str2_hash = str1_hash[str2]
                total = sum(str2_hash.values())
                for key in str2_hash.keys():
                    prob = float(str2_hash[key])/total
                    result.append((key,prob))
        return result
    
    def print_2(self,ahead_list):
        result = ''
        unique = sorted(set([x[1] for x in ahead_list]),reverse=True)
        for prob in unique:
            tmp = [tup[0] for tup in ahead_list if tup[1]==prob]
            tmp.sort()
#            print tmp
            for word in tmp:
                s = "%s,%.3f;" %(word,prob)
                result += s
        #remove the trialing semicolon
        return result[:-1]
    
    def ahead(self,word,word2):
        l = self.look_ahead(word,word2)
        print self.print_2(l)



text = """Mary had a little lamb its fleece was white as snow;
And everywhere that Mary went, the lamb was sure to go. 
It followed her to school one day, which was against the rule;
It made the children laugh and play, to see a lamb at school.
And so the teacher turned it out, but still it lingered near,
And waited patiently about till Mary did appear.
"Why does the lamb love Mary so?" the eager children cry;"Why, Mary loves the lamb, you know" the teacher did reply."
"""

lines =text.splitlines()
BG = Bigram()
TG = Trigram()
for line in lines:
    BG.insertLine(line)
    TG.insertLine(line)
#currently we only handle the bigram case

import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = open("typeAheadInput.txt",'r')
for test in test_cases:
    if test == '\n':
        continue
    test=test.strip()
    opts = test.split(',')
    if opts[0]=='2':
        BG.ahead(opts[1])
    else:
        words = opts[1].split(" ")
        TG.ahead(words[0], words[1])

test_cases.close()

