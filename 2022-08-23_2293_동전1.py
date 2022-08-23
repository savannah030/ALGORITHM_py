# 1시간,, 못품

import sys
input = sys.stdin.readline

# n가지종류, 합 k원 만들기
n,k = map(int,input().split()) # 합 1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000
coins = []
dp = [0]*(k+1) # 0원부터 시작 
dp[0]=1
for _ in range(n):
    coins.append(int(input()))
#coins.sort()

for coin in coins:
    for i in range(1,k+1):
        if i-coin>=0:
            dp[i] += dp[i-coin]
print(dp[k])