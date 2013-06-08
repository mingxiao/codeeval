def form_dict(lines):
    """
    Given a list of lines, return a dictionary mapping from 
    circuit/jugg --> [H, E,P]
    """
    d = {}
    for line in lines:
        line = line.strip()
        info = line.split(' ') 
        d[info[1]] = form_list(info[2],info[3],info[4])
    return d

def prefs(lines):
    d = {}
    for line in lines:
        line = line.strip()
        info = line.split()
        pref = info[5].split(',')
        d[info[1]] = pref
    return d

def still_room(clist,max):
    """
    Returns true if there is still room
    """
    assert type(clist) == type([])
    return len(clist) < max

def next_circuit(pref,proposed):
    """
    Given a list of preferences and circuits already proposed,
    return the next ciruit that has not been proposed to
    """
    for c in pref:
        if c not in proposed:
            return c
    print 'returned NONE'

def better_match(clist,jdot):
    assert type(clist) == type([])
    for item in clist:
        if jdot > item[1]:
            return True
    return False

def worst_member(clist):
    assert type(clist) == type([])
    for i in range(len(clist)):
        if i == 0:
            worst = clist[i]
        else:
            if clist[i][1] < worst[1]:
                worst = clist[i]
    return worst

def match(circuit,jugglers,prefs):
    """
    Stable marraige problem, match jugglers to circuits.
    If first match based on pref. If the circuit is full, then
    we use the dot product to determine which one gets kicked out.
    
    circuit - dictionary. circuit --> [H,E,P]
    juggler - dictionary. juggler --> [H,E,P]
    prefs - dictionary. juggler --> [C1,C2,C3]
    """
    maxj = len(jugglers)/len(circuit) #max jugglers per circuit
    jfree = jugglers.keys()
    proposed = {} # juggler --> [circuits proposed]
    for jug in jfree:
        proposed[jug] = []
    match = {} # circuit --> [ (jug,score),...  ]
    for c in circuit:
        match[c] = []
    #print 'MATCHING'
    while len(jfree) != 0:
        jug = jfree.pop()
        #print 'current juggler',jug
        assert jug in jugglers
        assert jug in prefs
        cir = next_circuit(prefs[jug],proposed[jug])
        assert cir in circuit
        proposed[jug].append(cir)
        d = dot(jugglers[jug],circuit[cir])
        if still_room(match[cir],maxj):
            #print 'putting %s in %s'%(jug,cir)
            match[cir].append((jug,d))
        elif better_match(match[cir],d):
            assert len(match[cir]) == maxj
            #maybe its not the worst member that needs to be replaced
            #maybe its a combination of preference and score...
            worst = worst_member(match[cir])
            match[cir].remove(worst)
            jfree.append(worst[0])
            match[cir].append((jug,d))
        else:
            jfree.append(jug)
            pass
            #nothing changes
    return match

def ans(match, cirno):
    """
    Given a dictionary of circuit --> [(J1,30),...], and the circuit number
    return the sum of the Js in that circuit
    """
    cname = 'C{}'.format(cirno)
    assert cname in match
    lst = match[cname]
    ans = 0
    for tup in lst:
        ans += tup[1]
    return ans

def form_list(H,E,P):
    l = []
    l.append(int(H.split(':')[1]))
    l.append(int(E.split(':')[1]))
    l.append(int(P.split(':')[1]))
    return l

def dot(l1,l2):
    """
    Given two list, return the dot product
    """
    assert len(l1) == len(l2)
    return sum([a*b for a,b in zip(l1,l2)])


import sys
testcase = open(sys.argv[1],'r')
clines = []
jlines = []
for line in testcase:
    if line.startswith('C'):
        clines.append(line)
        pass
    elif line.startswith('J'):
        jlines.append(line)
        pass
testcase.close()
circuits = form_dict(clines)
jugglers = form_dict(jlines)
pref = prefs(jlines)

m = match(circuits, jugglers,pref)
print ans(m,1970)
