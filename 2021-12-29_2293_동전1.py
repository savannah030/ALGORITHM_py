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

# 예제 1: 1,2,5원으로 10원 만들기
##### coin=1일 때
# dp = [1, 1,1,1,1,1, 1,1,1,1,1] 경우의수 = [ (), (1), (1+1), (1+1+1), (1+1+1+1), (1+1+1+1+1), (1+1+1+1+1+1), (1+1+1+1+1+1+1), ... ] 
##### coin=2일 때
# dp = [1, 1,1,1,1,1, 1,1,1,1,1] 경우의수 = [ (), (1), (1+1,0+2), (1+1+1,1+2), (1+1+1+1,1+1+2), (1+1+1+1+1,1+1+1+2)] 
for coin in coins:                  # 예)
    for sum in range(1,k+1):        # dp[sum] 차례대로 탐색
        # dp[sum] 경우의수는 dp[sum-coin] 경우의수에 coin만 더하면 되니까 dp[sum]+=dp[sum-coin] 
        # 근데 sum-coin은 당연히 음수면 안되니까 조건문 붙인거고!
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
    