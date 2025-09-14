import sys
n = int(input())
sticks = [int(sys.stdin.readline())for _ in range(n)]

count = 1
last = sticks[-1]
for i in sticks[::-1]:
    if i > sticks[-1] and i > last:
        last = i
        count+=1

print(count)