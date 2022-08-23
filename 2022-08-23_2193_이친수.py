# 11분 100%에서 런타임 에러 -> N==1일 때 수정
import sys
input = sys.stdin.readline

N = int(input())
if N==1: print(1)
else:
    dp = [ [0]*2 for i in range(N+1) ] # dp[i][j] = i자리가 j일 때 이친수 개수

    '''
    dp[1][0] = 0
    dp[1][1] = 1
    dp[2][0] = dp[1][1]
    dp[2][1] = 0
    dp[3][0] = dp[2][0] + dp[2][1]
    dp[3][1] = dp[2][0]
    ...
    '''
    dp[1][1],dp[2][0]=1,1 # "1", "10" #dp[1][0],dp[2][1]은 만족하는 이친수 없음
    for i in range(3,N+1):
        dp[i][0] = dp[i-1][0]+dp[i-1][1]
        dp[i][1] = dp[i-1][0] # 1은 연속해서 나타나지 않음
        
    print(dp[N][0]+dp[N][1])
    