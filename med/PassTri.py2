

def next(prevMax,cur):
    if len(prevMax) == 0:
        return cur
    ans = [0]*len(cur)
    for i in range(len(cur)):
        if i==0:
            ans[0] = cur[0] + prevMax[0]
        elif i == len(cur)-1:
            ans[len(cur)-1] = cur[-1]+prevMax[-1]
        else:
            ans[i] = max(cur[i]+prevMax[i],cur[i]+ prevMax[i-1])
    return ans

def tolist(st):
    return [int(x) for x in st.split()]

import sys

test_cases = open(sys.argv[1], 'r')
prevMax = []
for test in test_cases:
    test = test.strip()
    prevMax = next(prevMax,tolist(test))
    pass

test_cases.close()
print max(prevMax)
