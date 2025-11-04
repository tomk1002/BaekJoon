import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

def dfs(index, current_sum):
    global count
    if index == N:
        return
    current_sum += nums[index]
    if current_sum == S:
        count += 1
    # 현재 원소 포함
    dfs(index + 1, current_sum)
    # 현재 원소 미포함
    dfs(index + 1, current_sum - nums[index])

dfs(0, 0)
print(count)