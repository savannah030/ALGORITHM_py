# 16분
import sys
input = sys.stdin.readline

answer = 0
N = int(input())
dp = [ -1 for _ in range(5001)]
dp[3],dp[5]=1,1

# 경우 나눠서 생각하기
for K in range(6,N+1):
    if dp[K-3]>=0 and dp[K-5]>=0:
        dp[K] = min(dp[K-3]+1,dp[K-5]+1)
    elif dp[K-3]>=0 and dp[K-5]<0:
        dp[K] = dp[K-3]+1
    elif dp[K-3]<0 and dp[K-5]>=0:
        dp[K] = dp[K-5]+1
print(dp[N])