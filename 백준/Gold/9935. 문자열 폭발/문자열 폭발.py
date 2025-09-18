import sys

line = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

# bomb identifier
blen = len(bomb)
bend = bomb[-1]
stk = []


for i in range(len(line)):
    stk.append(line[i])
    if len(stk) >= blen and stk[-1]==bend:
        isbomb = True
        for j in range(blen):
            if stk[len(stk)-blen+j] != bomb[j]:
                isbomb = False
        if isbomb:
            for _ in range(blen):
                stk.pop()
if not stk:
    print('FRULA')
else:
    print(*stk,sep='')