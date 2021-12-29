# https://mong9data.tistory.com/68
import sys
input = sys.stdin.readline

# n가지종류, 합 k원 만들기
n,k = map(int,input().split()) # 합 1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000

dp = [0]*(k+1) # 0원부터 시작 
dp[0]=1 ########### 동전이 하나만 쓰일 때 dp[0]값인 1을 이용

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

# 1로만 이루어진 애들 먼저 만들고(1,1+1,1+1+1,...)
# 그다음 (1+2,1+1+2,1+1+1+2,...) 이런식으로
for coin in coins:
    for sum in range(1,k+1):
        if sum-coin>=0:
            dp[sum] += dp[sum-coin] 
print(dp[k])

'''
# 처음에는 밑의 방법으로 풀려고 했는데 그러면 순서만 다른 경우는 거르지 못함 
for coin in coins:
    dp[coin] += 1
for i in range(1,k+1):
    for coin in coins:
        dp[i] += dp[i-coin]
'''
    