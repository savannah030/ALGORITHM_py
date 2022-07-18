import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1) # dp[i]=i를 1로 만드는 데에 필요한 연산 횟수
# dp[2],dp[3] 미리 초기화하면 런타임 에러
for num in range(2,N+1):
    dp[num] = dp[num-1]+1
    # elif말고 if문 써서 거를 수 있도록
    if num%3==0:
        dp[num] = min(dp[num], dp[num//3]+1)
    if num%2==0:
        dp[num] = min(dp[num], dp[num//2]+1) 
print(dp[N])