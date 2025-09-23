
import sys
from collections import deque

def BFS(start):
    q = deque([start])
    visited[start] = 1
    while q:
        u = q.popleft()
        for v in arr[u]:
            if visited[v] == 0:
                visited[v] = -visited[u]
                q.append(v)
            elif visited[v] == visited[u]:
                return False
    return True


n = int(sys.stdin.readline())

for _ in range(n):
    V,E = map(int,sys.stdin.readline().split())

    arr = [[] for _ in range(V+1)]

    for _ in range(E):
        u,v = map(int,sys.stdin.readline().split())
        arr[u].append(v)
        arr[v].append(u)
    
    visited = [0]*(V+1)

    result = True
    for i in range(1,V+1):
        if visited[i] == 0:
            if not BFS(i):
                result = False
                break
    
    print('YES' if result else 'NO')