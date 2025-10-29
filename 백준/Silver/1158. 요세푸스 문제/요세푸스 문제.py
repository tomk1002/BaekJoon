import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

res = []
nums = deque(range(1,N+1))

while nums:
    for _ in range(K-1):
        nums.append(nums.popleft())
    res.append(nums.popleft())

print('<' + ', '.join(map(str,res)) + '>')