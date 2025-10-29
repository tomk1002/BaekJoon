import sys
input = sys.stdin.readline

N = int(input())
stack = []
res = []
impossible = False
current = 0

for _ in range(N):
    target = int(input())
    while current < target:
        current+=1
        stack.append(current)
        res.append('+')
    
    if stack[-1] == target:
        stack.pop()
        res.append('-')
    else:
        impossible = True
        break

if impossible:
    print("NO")
else:
    print(*res,sep='\n')
