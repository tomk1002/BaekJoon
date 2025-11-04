import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, N + 1):  # 1부터 N까지 부분집합
    for comb in combinations(nums, i):
        if sum(comb) == S:
            count += 1

print(count)