import sys
input = sys.stdin.readline

N,K = map(int,input().split()) # 물건개수(<=100),들수있는최대무게(<=100000)
things = [(-1,-1)]
for _ in range(N):
    things.append(tuple(map(int,input().split()))) #(무게,가치)

# dp[i][j] i번째 물건을 넣었을때/안넣었을 때 무게 j(<=K)에 따라 얻을 수 있는 최대 가치 
# 따라서 dp[i][j]에서 things[i][0]>j일 때는 고려하지 않는다. (아예 넣을 수 없다)
# 넣을 수 있다면 max(현재 넣을 물건 무게만큼 빼고 현재 물건을 넣을 때의 가치,이전 배낭 그대로 가지고 갈 때의 가치)
dp = [ [0]*(K+1) for _ in range(N+1)] 
for i in range(1,N+1):
    W,V = things[i]
    for j in range(1,K+1):
        if W>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-W]+V,dp[i-1][j]) #max(현재물건을 넣었을 때, 안넣었을 때)

print(dp[N][K])

