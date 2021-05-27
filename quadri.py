import pandas as pd
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}
list=[]
dict={}
dicti={}

def infix_to_postfix(formula):
    stack = []
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack: 
        output += stack.pop()
    print(f'POSTFIX: {output}')
    return output

def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRI[ch] <= PRI[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append( op+b+a )
            op_stack.append(ch)
    
    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append( op+b+a )
    print(f'PREFIX: {exp_stack[-1]}')
    return exp_stack[-1]


def generate3AC(pos):
    print("THREE ADDRESS CODE GENERATION - ")
    exp_stack = []
    t = 0
    
    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
            list.append(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
            exp_stack=exp_stack[:-2]
            exp_stack.append(f't{t}')
            t+=1

expres = input("INPUT THE EXPRESSION: ")
pos = infix_to_postfix(expres)
pre = infix_to_prefix(expres)
generate3AC(pos)

print("Quadruple - ")

print("OP "+" Agr1 "+" Agr2 "+" Result ")
c = 0
co=10010
for i in list:
    x = i.split(" ")
    for j in x:
        if j in OPERATORS:
            print(j,"  ",end = " ");
            print(x[2],"   ",x[4]+"     "+x[0])
            dict[x[0]] = c
            dicti[c] = co
    c+=1
    co+=1

print("Triple - ")
print("      ","OP    "+" Agr1   "+" Agr2 ")
for i in list:
    x = i.split(" ")
    for j in x:
        if j in OPERATORS:
            print("[",dict[x[0]],"]  ",end = " ")
            print(j,"    ",end = " ");
            if x[2] in dict.keys() and x[4] in dict.keys():
                print("[",dict[x[2]],"]    [",dict[x[4]],"]")
            elif x[2] in dict.keys():
                print("[",dict[x[2]],"]    ",x[4])
            elif x[4] in dict.keys():
                print(x[2],"    [",dict[x[4]],"]")
            else:
                print(x[2],"    ",x[4])

print("Indirect triple - ")
print("        ","OP   "+" Agr1      "+" Agr2 ")
for i in list:
    x = i.split(" ")
    for j in x:
        if j in OPERATORS:
            print("[",dicti[dict[x[0]]],"]  ",end = " ")
            print(j,"  ",end = " ");
            if x[2] in dict.keys() and x[4] in dict.keys():
                print("[",dicti[dict[x[2]]],"]      [",dicti[dict[x[4]]],"]")
            elif x[2] in dict.keys():
                print("[",dicti[dict[x[2]]],"]     ",x[4])
            elif x[4] in dict.keys():
                print(x[2],"      [",dicti[dict[x[4]]],"]")
            else:
                print(x[2],"       ",x[4])
