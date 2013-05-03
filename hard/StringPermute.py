'''
Created on Jul 14, 2012

@author: mingxiao10016
'''

#recursive definition. 
def permute(word):
    if len(word) == 1:
        return [word]
    else:
        # we want to take the first letter 
        # and put it in between each of the letters in each of the words
        # in the permutation of the rest of the word
        result = []
        rest = permute(word[1:])
#        print rest
        first = word[0]
        for token in rest:
            for i in range(len(token)):
                result.append(token[:i]+first+token[i:])
            result.append(token+first)
        return result
    
# formats the permList into the correct output
def format_list(permList):
    ans = ''
    for perm in permList:
        ans += perm +','
    return ans[:-1]

def print_permute(word):
    return format_list(sorted(permute(word)))


import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = open("permuteInput.txt", 'r')
for test in test_cases:
    if test=='\n':
        continue
    test =test.strip()
    print print_permute(test)

test_cases.close()

