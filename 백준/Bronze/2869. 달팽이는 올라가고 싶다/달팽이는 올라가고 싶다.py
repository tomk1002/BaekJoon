a,b,v = map(int,input().split())

n = (v-b)/(a-b)

if n <1:
    print(0)
elif n>round(n):
    print(round(n+1))
else:
    print(round(n))