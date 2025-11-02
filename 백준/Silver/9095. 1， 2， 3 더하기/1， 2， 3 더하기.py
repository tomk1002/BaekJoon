import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    m = int(input())
    dp = [1, 1, 2, 4]
    if m < 4: 
        print(dp[m])
    else:
        for _ in range(4,m+1):
            dp[0] = dp[1] + dp[2] + dp[3]
            dp[1] = dp[2]
            dp[2] = dp[3]
            dp[3] = dp[0]
        print(dp[0])