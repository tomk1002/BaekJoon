import sys

M, N, D = map(int,input().split())
spot = list(map(int,sys.stdin.readline().split()))
animals = [list(map(int,input().split())) for _ in range(N)]
spot.sort()

def in_range(spot,loc,range):
    x,y = loc
    if range >= abs(spot-x)+y:
        return True
    else:
        return False

# 사로 index
count = 0

for loc in animals:        
    L = -1
    R = M
    # loc[0]에 가장 가까운 사로(spot[i]) = center을 계산해주는 while 문
    while L+1 < R:
        center = (L+R)//2
        if loc[0] > spot[center]:
            L = center 
        else:
            R = center

    if L == -1:
        if in_range(spot[R],loc,D):
            count+=1
    elif R == M:
        if in_range(spot[L],loc,D):
            count+=1
    else: 
        if in_range(spot[L],loc,D) or in_range(spot[R],loc,D):
            count+=1

print(count)

    
        
        

            

        


        

