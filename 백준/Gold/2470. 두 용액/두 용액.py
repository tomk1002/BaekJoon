import sys
n = int(input())
liq = list(map(int,sys.stdin.readline().split()))
liq.sort()

L = 0
R = n-1

a,b = liq[L],liq[R]
mix = a+b
best = abs(a+b)

while L < R:
    mix = liq[L] + liq[R]

    if abs(mix) < best:
        a,b= liq[L],liq[R]
        best = abs(mix)
        if mix == 0:
            break;
    
    if mix < 0:
        L += 1
    else:
        R -=1

print(a,b)