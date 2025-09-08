def move(n,x,y):
    if n >1:
        #n-1개를 시작장대(x)에서 보조장대(6-x-y)로 옮긴다.
        move(n-1,x,6-x-y)
        #다 옮겼으면 n판을 시작(x)에서 끝(y)로 옮긴다.
        print(x,y)
        #끝장대가 다시 비었으면 보조장대(6-x-y)에 있는n-1개를 끝장대(y)로 옮긴다.
        move(n-1,6-x-y,y)   
    if n==1:
        #n이 1일 때도 큰 거 하나가 남은거니 y로 옮긴다.
        print(x,y)
        


n = int(input())

if n > 20:
    print(2**n-1)
else:
    print(2**n-1)
    move(n,1,3)