import sys 
from collections import deque
input = sys.stdin.readline

N, M  = map(int,input().split())

arr = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    u,v = map(int,input().split())
    arr[u].append(v)
    indegree[v] +=1;

line = deque([])
result = []

for i in range(1,N+1):
    if indegree[i] == 0: line.append(i)

while line:
    n = line.popleft()
    result.append(n)

    for connected in arr[n]:
        indegree[connected] -=1
        if indegree[connected] == 0:
            line.append(connected)
print(*result)