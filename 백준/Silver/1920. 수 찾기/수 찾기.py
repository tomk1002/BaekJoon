import sys

x = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
y = int(input())
m = list(map(int, sys.stdin.readline().split()))

def bin_search(a,n):
    pl = 0
    pr = len(a)-1

    while pl <= pr:
        pc = (pl+pr)//2
        if n == a[pc]:
            return True
        if n > a[pc]:
            pl = pc+1
        else:
            pr = pc-1
    return False
    
for num in m:
    if bin_search(a,num):
        print(1)
    else:
        print(0)