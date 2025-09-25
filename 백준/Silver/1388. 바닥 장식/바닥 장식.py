import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
floor = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# 한번에 그래프에 표시하기 어려울듯
# 다음 타일이 같은 타일이면 연속 검사 진행 필요 ==> 재귀(DFS)
# 일방향 행이동, 열이동 이기 때문에 dx,dy필요 없음.
def dfs(y, x):
    # 들어오면서 출첵
    # 컴퓨터는 행열 기준 위치 파악하기 때문에 y,x로
    visited[y][x] = 1
    type = floor[y][x]
    if type == '-': #가로타일
        nx = x + 1
        #일단 최대 가로열 길이 초과 X, 다음 칸 동일한지 확인, 방문 안해본건지 확인
        if nx < M and floor[y][nx] == '-' and not visited[y][nx]:
            dfs(y, nx)
    else: #세로타일
        ny = y + 1
        if ny < N and floor[ny][x] == '|' and not visited[ny][x]:
            dfs(ny, x)
#하나씩 돌면서 해야겠는데?
count = 0
for i in range(N):
    for j in range(M):
        # 한 칸씩 순회하면서, 방문안해본거면 dfs 돌려서 같은 타일 방문표시 다 돌리면서 +1, 방문한거면 카운트 안해서 중복 안됨
        if not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)