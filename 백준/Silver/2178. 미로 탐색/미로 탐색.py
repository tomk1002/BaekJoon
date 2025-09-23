import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

def BFS(x, y):
    # 이동할 상, 하, 좌, 우 방향 정의
    # 각 index 값마다 dx,dy중 하나만 값이 있다면 순서 및 배치는 무관함
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    # 왜 queue = deque((x,y))는 안될까?
    # python의 container는 iterable를 직접 넣을 때 자동으로 iterable을 풀어서 원소 단위로 저장을 한다. 따라서 (x,y)를 한쌍으로 넣고 싶을 경우 따로 append, add 등을 실행하는 것이 맞다.
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 상하좌우 이동시 다음 포지션(nx,ny)의 이동가능여부 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # Grid Boundary(맵)을 벗어나선 안됨
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            # 벽(0으로 이루어진 부분)으로 이동 불가
            if graph[nx][ny]==0:
                continue
            # 제약 조건으로부터 자유로우니 이동 가능한 길 확인
            if graph[nx][ny]==1:
                # +1 값을 통해 이동한 칸에 현재 움직임 수를 저장
                graph[nx][ny] = graph[x][y]+1
                # 이동칸 queue에 넣으면서 while loop 반복하기.
                queue.append((nx,ny))

    # 마지막 값에서 카운트 값 뽑기 
    # 시작 좌표는 (1,1)이지만 grid상 좌표(0,0)시작 고려해서 -1
    return graph[N-1][M-1]

print(BFS(0,0))