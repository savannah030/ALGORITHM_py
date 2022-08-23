import sys
input = sys.stdin.readline
INF = int(1e9+1)
N = int(input())
if N==1:
    print(0)
elif N==2 or N==3:
    print(1)
else:
    dp = [INF]*(N+1)
    dp[2],dp[3]=1,1
    for n in range(4,N+1):
        dp[n] = min(dp[n],dp[n-1]+1)
        if n%3==0:
            dp[n] = min(dp[n//3]+1,dp[n])
        if n%2==0:
            dp[n] = min(dp[n//2]+1,dp[n])
    print(dp[N])