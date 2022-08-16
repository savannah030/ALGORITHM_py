# 10분
import sys
input = sys.stdin.readline

costs = []
N = int(input())
for _ in range(N):
    costs.append(list(map(int,input().split())))
    
# dp[i][0] = i번째 집이 빨강인 경우
# dp[i][1] = i번째 집이 초록인 경우
# dp[i][2] = i번째 집이 파랑인 경우
# 매 i마다 최솟값 구해야 모든 집을 칠하는 비용의 최솟값 구할 수 있음
dp = [ [0,0,0] for _ in range(N) ] 
dp[0] = costs[0][:]
for i in range(1,N):
    dp[i][0] = min(dp[i-1][1]+costs[i][0],dp[i-1][2]+costs[i][0])
    dp[i][1] = min(dp[i-1][0]+costs[i][1],dp[i-1][2]+costs[i][1])
    dp[i][2] = min(dp[i-1][0]+costs[i][2],dp[i-1][1]+costs[i][2])
print(min(dp[N-1]))
    