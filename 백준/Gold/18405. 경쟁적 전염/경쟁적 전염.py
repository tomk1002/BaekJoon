import sys
input = sys.stdin.readline

# NORTH KOREA?
N,K = map(int,input().split())

# 혹시 바이러스는 탄저균?
testube = [list(map(int,input().split())) for _ in range(N)]

# SEXY?
S,X,Y = map(int,input().split())

# 주어진 좌표 (X,Y)에서 가장 가까운 바이러스를 구하자!
# 바이러스 별로 (X,Y)에서 출발해서 최단 경로(턴 수) 구하기
# 만약 같다면 최소 숫자 바이러스


# 바이러스 위치 구하기
viruses = []
virus_location = []
# testube 훑으며 바이러스 좌표 찾아주기
for i, row in enumerate(testube):
    for j, val in enumerate(row):
        if testube[i][j] != 0:
            # 빈칸이 아니면 바이러스 숫자 및 x,y 좌표 추가
            virus_location.append((testube[i][j],i+1,j+1))
# 바이러스별 거리?
distances = []
for i,x,y in virus_location:
    dist = abs(X-x) + abs(Y-y)
    distances.append((dist,i))
# S 초 지난 후에 바이러스 도달 못했으면 0을 프린트해야함.
# 일단 가장 가까운 거리
closest_distance = min(distances)[0]

# 바이러스들이 가장 가까운 거리를 고유할 떄
# 제일 가까운 애들 둘만 비교?
closest2 = sorted(distances)[:2]

# 가까운 애들 중 바이러스 숫자 작은 애 찾기
if closest2[0][0] > closest2[1][0]:
    nearest_virus = closest2[1][1]
else:  
    nearest_virus = closest2[0][1]

if S<closest_distance:
    print(0)
else:
    print(nearest_virus)
    