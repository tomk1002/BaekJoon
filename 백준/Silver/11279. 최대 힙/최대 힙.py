import heapq
import sys
n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0 and not numbers:
        print(0)
    elif num!= 0:
        heapq.heappush(numbers,-num)        
    else:
        print(-heapq.heappop(numbers))