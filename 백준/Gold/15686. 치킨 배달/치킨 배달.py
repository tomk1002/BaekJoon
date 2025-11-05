import sys
input = sys.stdin.readline

N, M = map(int,input().split())
cmap = [list(map(int,input().split())) for _ in range(N)]
chicken_zip = []
houses = []
# 일단 지도를 돌며 치킨집과 집들의 주소(좌표)를 모으기
for i in range(N):
    for j in range(N):
        if cmap[i][j] == 2:
            chicken_zip.append((i,j))
        if cmap[i][j] == 1:
            houses.append((i,j))


chosen = []
min_city_street = float('inf')
def dfs(start):
    global min_city_street

    if len(chosen) == M:
        city_street = 0
        for hx, hy in houses:
            city_street += min(abs(hx-cx)+abs(hy-cy) for cx,cy in chosen)
        min_city_street = min(city_street, min_city_street)
        return
    
    # 치킨집별로 넣어보거나 빼보거나
    for i in range(start, len(chicken_zip)):
        chosen.append(chicken_zip[i])
        dfs(i+1)
        chosen.pop()

dfs(0)
print(min_city_street)
