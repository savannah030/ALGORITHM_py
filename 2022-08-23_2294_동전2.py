# 1시간,, 못품

import sys
input = sys.stdin.readline
INF = int(1e9)+1
n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
    
dp = [INF]*(k+1) # dp[i] = i원을 만들 수 있는 동전 개수의 최솟값
dp[0] = 0

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i],dp[i-coin]+1)
    
if dp[k]==INF:
    print(-1)
else:
    print(dp[k])
    

'''
# 첫 풀이
# for coin마다 dp값 갱신되므로 또 for문 돌 필요없음(3중 for문 필요없음)
for coin in coins:
    for i in range(coin,k+1):
        if i%coin==0:
            dp[i] = min(dp[i],i//coin)
        else:
            dp[i] = min(dp[i],dp[i-1]+1) ###### i-1가 아니라 i-coin값을 가져온다고 발상했으면,,,
                                        
if dp[k]==INF:
    print(-1)
else:
    print(dp[k])
'''
