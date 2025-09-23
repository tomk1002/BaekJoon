import sys

def DFS(start):
    stk = [start]
    while stk:
        x = stk.pop()
        visited[x] = True
        for nxt in arr[x]:
            if not visited[nxt]:
                visited[nxt] = True
                if inout[nxt-1] == 1:
                    routes.append(1)
                elif inout[nxt-1] == 0:
                    stk.append(nxt)
            

N = int(sys.stdin.readline())

# get indoor/outdoor states - string ==> int list conversion
inout = list(map(int, sys.stdin.readline().rstrip()))

# get vertexes into adjacent list
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)


# 실내만이 시작과 끝. 실내 = 1, 실외 = 0
# 중간에 실내 있으면 X
# 실내 노드 기준으로 ㄱㄱ

routes = []
for j in range(1,N+1):
    visited = [False]*(N+1)
    if inout[j-1] == 1:
        DFS(j)

print(len(routes))

