import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
cmap = [list(map(int,input().split())) for _ in range(N)]

# 1. 치킨집 기준 or 가정집 기준?
# 2. 무엇을 어디에 더할 것인가? 치킨집에 가까운 집들과의 거리의 합을?
# 3. 폐점 시킬 치킨 집을 어떤 기준으로 정하고 남은 도시 치킨 거리는 어떻게 구할지.
# 4. 처음에 주어진 치킨집 n 개 중에, k 개를 제외한 치킨집을 임의로 선택했을 때 도시의 치킨 거리를 구하고.
# 5. 그 중에 최솟값을 구하면 되겠다.
# 6. 그렇다면 임의의 치킨집 i 개가 주어졌을 도시의 치킨 거리는 어떻게 구하는가?
# 7. 그래프를 순회하며 1을 만났을 시에 주어진 치킨집 별로 (좌표의 리스트로 주어짐) 거리를 구하고 그 중 최소를 선택

chicken_zip = []
houses = []
# 일단 지도를 돌며 치킨집과 집들의 주소(좌표)를 모으기
for i in range(N):
    for j in range(N):
        if cmap[i][j] == 2:
            chicken_zip.append((i,j))
        if cmap[i][j] == 1:
            houses.append((i,j))

chicken_stay = combinations(chicken_zip,M) # 남아 있는 치킨집들의 경우의 수

# 정답: chicken stay 중 도시 거리의 최솟값
# chicken stay별로 도시 거리를 측정하고
# 최솟값을 저장해야함
# chicken stay의 도시 거리를 어떻게 측정 할 수 있을까?
city_streets = []
for chicken_stores in chicken_stay: #남아 있는 치킨집들의 경우의 수
    city_street = 0 # 특정 경우의 수의 도시 거리
    for house in houses: # 집별로 순회하며
        chick_street = float('inf') # 집별 치킨거리를 구하기 위해 일단 최댓값 설정
        for store in chicken_stores: # 주어진 치킨 집들을 순회하며 거리를 비교
            dist = abs(house[0]-store[0]) + abs(house[1]-store[1])
            if dist == 1: # 거리가 1일 경우에 그보다 작을 수 없으니 굳이 다른 치킨집들 돌지말고 다음 집의 치킨 거리를 파악하기 위해
                chick_street = 1
                break
            if dist < chick_street: # 그 중 최소거리 = 해당 집의 치킨거리
                chick_street = dist
        city_street+= chick_street # 도시 거리에 치킨거리 합산
    city_streets.append(city_street) # 최소 도시 거리를 구하기 위해 도시거리 경우의 수에 더하기

print(min(city_streets))

        
