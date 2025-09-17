import sys
line = sys.stdin.readline()

tmp = 1
ans = 0
stk = []

for i in range(len(line)):

    if line[i] == '(':
        stk.append(line[i])
        tmp *= 2
    
    elif line[i] == ')':
        if not stk or stk[-1] == '[':
            ans = 0
            break
        elif line[i-1] == '(':
            ans += tmp
        stk.pop()
        tmp //=2

    elif line[i] == '[':
        stk.append(line[i])
        tmp *= 3

    elif line[i] == ']':
        if not stk or stk[-1] == '(':
            ans = 0
            break
        elif line[i-1] == '[':
            ans += tmp
        stk.pop()
        tmp //=3

if stk:
    print(0)
else:
    print(ans)