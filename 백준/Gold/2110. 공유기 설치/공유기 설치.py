import sys

# 필요한 데이터 fetch 후 sort
n, C = map(int,sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(n)]
houses.sort()

# 두 공유기 간의 거리의 최댓값을 좁혀나가는 이분 검색 
# 최소 최대는 오름차순 정렬된 집 x좌표의 양 끝 index
L,R = 1, houses[-1]-houses[0]

while L <= R: 
    mid = (L+R)//2
    # 첫번째 값부터 시작
    curr = houses[0]
    # 공유기 개수는 첫 집에 1개부터 시작
    cnt = 1
    # 두번째 집부터 마지막 집까지
    for i in range(1,n):
        # 현재 집의 x좌표에서 최대 거리를 더했을 때의 거리에 있는 집이라면 
        if houses[i] >= curr + mid:
            # 현재 집을 새로운 집으로 가정하고 공유기를 설치하고
            curr = houses[i]
            # 공유기 설치 개수를 하나 늘린다
            cnt +=1
        # 만약 현재 좌표+최대거리 미만의 거리에 있는 집이라면 공유기 설치가 되지 않는다.
    # 공유기의 개수가 최대 개수보다 같거나 많다면
    # 최대 거리가 여유가 있다는 말이기에 최솟값을 높힌채로 예상 평균 최댓값을 올리고 다시 while loop을 돌린다.
    if cnt >= C:
        L = mid + 1
        result = mid
    # 반면 공유기의 설치해야 하는 개수보다 적다는 말은 최대 거리가 여유가 없다는 말이기에
    # 최댓값을 낮춘채로 다시 while loop을 돌린다.
    else:
        R = mid -1

print(result)

