import sys
# get number of trees, total amount of wood needed
n, wood = map(int,input().split())
# get list of height of trees
trees = list(map(int,input().split()))
# sort height of trees from high to low for convenience
trees.sort()

# 높이 H에서 나무를 잘랐을 때 얻는 나무 총량을 구하는 함수
def cut(a, h):
    a.sort(reverse=True)
    total = 0
    for treeh in a:
        if treeh >=h:
            total+= treeh-h
        if treeh < h:
            break
    return total

# 최대 최소 중간 값 썰어보고 총량 비교해보면서 이분 검색
pl = 0
pr = max(trees)
Height = 0

while pl <= pr:
    mid = (pl + pr)//2
    got = cut(trees,mid)
    if got >= wood:
        Height = mid
        pl = mid+1
    else:
        pr = mid-1

print(Height)