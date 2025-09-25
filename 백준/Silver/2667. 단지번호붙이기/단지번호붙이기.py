import sys
input = sys.stdin.readline
N = int(input())

graph = []
for _ in range(N):
    rows = list(map(int,input().rstrip()))
    graph.append(rows)

visited = [[0]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y, x):
    stk = [(y,x)]
    visited[y][x] = 1
    count = 1
    while stk:
        cy,cx = stk.pop()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if not(0<= nx < N and 0<= ny < N):
                continue # 가독성 위해 분리
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                stk.append((ny,nx))
                count+=1
    return count

complexes = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            complexes.append(dfs(i,j))
            
print(len(complexes))
print(*sorted(complexes),sep='\n')

