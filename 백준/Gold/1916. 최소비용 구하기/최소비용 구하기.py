import sys
import heapq

input = sys.stdin.readline
N = int(input()) # number of cities (1 <= N <= 1,000)
M = int(input()) # number of buses (1 <= M <= 100,000)

routes = [[] for _ in range(N+1)]
for _ in range(M): 
    dep, arr, cost = map(int,input().split())
    routes[dep].append((arr,cost))
    # Departure / Arrival / Cost
    # Given in int

start,end = map(int,input().split())
# Starting City / End City
# Also given in int

#Dijkstra Algorithm
costs = [1e9 for _ in range(N+1)] # 노드별 초기 가중치합 무한대 설정
costs[start] = 0 # 시작 노드는 0
heap = [] # 왜 힙을 쓰는가? 가장 cost가 가장 작은 값이 나온다.
heapq.heappush(heap,[0,start]) # 출발지 추가 - 이때 cost를 0번 index에 두는 것이 중요하다.
                               # 그래야 우리가 원하는 cost위주 힙정렬이 가능하다

while heap:
    cur_cost, cur_v = heapq.heappop(heap) # 탐색 시작할 현재 비용, 현재 노드
    # cost가 0번 index기 때문에 cur_cost가 먼저 unpack된다
    if costs[cur_v] < cur_cost: # 기존 최소비용보다 크다면 무시
        continue
    for next_v, next_cost in routes[cur_v]: # 인접노드 검색
        sum_cost = cur_cost + next_cost # 인접 노드까지 비용 합산
        if sum_cost >= costs[next_v]: # 인접 노드까지의 비용이 기존 비용보다 크다면 무시
            continue
        costs[next_v] = sum_cost # 기존 비용보다 적다면 갱신
        heapq.heappush(heap,[sum_cost, next_v]) # 다음 계산을 위한 큐 삽입

print(costs[end])