import sys
n = int(sys.stdin.readline())
# nums1 = list(map(int,sys.stdin.readline().split()))
nums1 = set(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
nums2 = list(map(int,sys.stdin.readline().split()))

ans = []
for num in nums2:
    if num in nums1:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)