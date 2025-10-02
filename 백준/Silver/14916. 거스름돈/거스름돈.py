n = int(input())
if n==1 or n==3:
    print(-1)
elif n%5 == 0:
    print(n//5)
else:
    count = 0
    while n%5 != 0:
        n-=2
        count+=1
    count += n//5
    print(count)