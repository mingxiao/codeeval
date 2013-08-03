"""
ISSUE need to account for the unary - operator
as in -(48)
A unary operator is the first token or any operator that is preceded by another operator (not parentheses).
"""

import re
#a lower number has HIGHER precedence
PREC = {'+':5,'-':5,'*':4,'/':4,'^':3, 'NEGATE':2}
ASSOC = {'^':"RIGHT",'*':"LEFT",'/':"LEFT",'+':'LEFT','-':'LEFT','NEGATE':'RIGHT'}

def get_tokens(expr_str):
    ops = '*\(\)+-^/'
    tokens =  re.findall('\d+\.\d+|\d+|[%s]'%ops,expr_str)
    # now differentiate between minus and negate
    for i in range(len(tokens)):
        if tokens[i] == '-':
            if i == 0:
                tokens[i] = 'NEGATE'
            elif tokens[i-1] in PREC or tokens[i-1]=='(':
                tokens[i] = 'NEGATE'
    return tokens

def prec(tok1,tok2):
    """
    Returns True if tok1 has higher or equal precedence than tok
    """
    global PREC
    assert tok1 in PREC
    assert tok2 in PREC
    return PREC[tok1] <= PREC[tok2]

def shunting_yard(tokens):
    global PREC
    global ASSOC
    output= []
    opstack= []
    while len(tokens) > 0:
        ctoken = tokens.pop(0)
        #operator
        if ctoken == '(':
            opstack.append(ctoken)
        elif ctoken == ')':
            top = opstack.pop()
            while top != '(':
                output.append(top)
                if len(opstack) == 0:
                    raise Exception('mismatched parens')
                top = opstack.pop()
        elif ctoken in PREC:
            #+,-,*,/
            oplen = len(opstack)
            while oplen >0: 
                top = opstack[oplen-1]
                if top not in PREC:
                    break
                if (ASSOC[ctoken]=='LEFT' and PREC[ctoken]==PREC[top]) or PREC[ctoken] > PREC[top]:
                    output.append(opstack.pop())
                    oplen -= 1
                else:
                    break
            opstack.append(ctoken)
        else:
            #so far, if its not an operator, then its a number
            output.append(ctoken)
    while len(opstack) > 0:
        if opstack[-1] == '(' or opstack[-1] == ')':
            raise Exception('mismatched parens!')
        output.append(opstack.pop())
    return output

def eval_rpn(tokens):
    """
    evaluates a list of tokens in reverse polish notation. returns a float
    """
    global PREC
    stack = []
    while len(tokens) > 0:
        top = tokens.pop(0)
        if top == '+':
            op1 = float(stack.pop())
            op2 = float(stack.pop())
            stack.append(op1+op2)
        elif top == '-':
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1-op2)
        elif top == '*':
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1*op2)
        elif top == '/':
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1/op2)
        elif top == '^':
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            stack.append(op1**op2)
        elif top == 'NEGATE':
            op = float(stack.pop())
            stack.append(-1*op)
        else:
            #assume its a number and push it onto the stack
            stack.append(top)
#    print 'STACK',stack
    assert len(stack) == 1
    return stack.pop()

def truncate_float(fl):
    fl = round(fl,5)
    if fl == int(fl):
        return int(fl)
    else:
        return fl

import sys
test_cases = open(sys.argv[1],'r')
for test in test_cases:
    test = test.strip()
    tokens = get_tokens(test)
    rpn = shunting_yard(tokens)
    ans = eval_rpn(rpn)
    print truncate_float(ans)
test_cases.close()

