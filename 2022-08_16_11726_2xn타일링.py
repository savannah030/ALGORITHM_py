# 9분
import sys
input = sys.stdin.readline

n = int(input())
if n==1:
    print(1)
else:
    dp = [0]*(n+1)
    dp[1],dp[2]=1,2

    # dp[i-2]+가로타일 2개 붙일 때만 고려해야함
    # dp[i-2]+세로타일2개는 dp[i-1]랑 겹침!
    for i in range(3,n+1):
        dp[i] = dp[i-2]+dp[i-1]
        
    print(dp[n]%10007)
