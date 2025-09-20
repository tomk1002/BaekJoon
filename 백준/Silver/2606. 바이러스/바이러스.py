import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False]*(n+1)


que = deque([1])
    
while que:
    node = que.popleft()
    for nxt in arr[node]:
        if visited[nxt] == False:
            que.append(nxt)
            visited[nxt] = True

count = 0
for i in visited[2:]:
    if i == True:
        count+=1
print(count)