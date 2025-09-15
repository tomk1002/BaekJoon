import sys

def bs(arr,x):
    L, R = -1, len(arr)

    while L+1 < R:
        mid = (L+R)//2
        if  arr[mid] < x:
            L = mid
        else:
            R = mid
    return R

n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
longest = [nums[0]]
for i in range(n):
    if nums[i]> longest[-1]:
        longest.append(nums[i])
    else:
        idx = bs(longest,nums[i])
        longest[idx] = nums[i]

print(len(longest))



