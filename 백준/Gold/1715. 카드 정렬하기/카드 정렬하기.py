import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    heapq.heappush(heap,int(sys.stdin.readline()))

total = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    total += a+b
    heapq.heappush(heap,(a+b))

print(total)
