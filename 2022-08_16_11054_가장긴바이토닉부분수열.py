import sys
input = sys.stdin.readline

# 내 풀이
# 거꾸로 돌아가기,,,, O(2*N(N+1)/2) N=1000이므로 충분히 가능
def my_solution():
    # 33분 
    # 41분 디버깅
    N = int(input())
    A = list(map(int,input().split())) # 수열

    # dp[i] i를 선택했을 때 가장 긴 수열 길이(왼쪽부터 탐색) 
    dp = [1]*N
    for i in range(1,N):
        for j in range(i-1,-1,-1):
            if A[i]>A[j]:
                dp[i] = max(dp[i],dp[j]+1) 

    # dp2[i] i를 선택했을 때 가장 긴 수열 길이(오른쪽부터 탐색) 
    dp2 = [1]*N
    for i in range(N-1,-1,-1):
        for j in range(i+1,N):
            if A[i]>A[j]:
                dp2[i] = max(dp2[i],dp2[j]+1)

    answer = 0
    for i in range(N):
        answer = max(answer,dp[i]+dp2[i]-1) # 자기자신 빼야함
    print(answer)


# 다른풀이참고
# O(N(N+1)/2) # 한번에 비교
def others_solution():

    N = int(input())
    A = list(map(int,input().split())) # 수열
    A_reverse = A[::-1]

    # dp[i] i를 선택했을 때 가장 긴 수열 길이(왼쪽부터 탐색)
    # dp2[i] i를 선택했을 때 가장 긴 수열 길이(오른쪽부터 탐색한 결과를 순차적으로 저장. 따라서 뒤집힌 모양) 
    dp = [1]*N
    dp2 = [1]*N 
    for i in range(N):
        for j in range(i):
            if A[i]>A[j]:
                dp[i] = max(dp[i],dp[j]+1) 
            if A_reverse[i]>A_reverse[j]:
                dp2[i] = max(dp2[i],dp2[j]+1) 
                
    dp2 = dp2[::-1]
    answer = 0
    for i in range(N):
        answer = max(answer,dp[i]+dp2[i]-1) # 자기자신 빼야함
    print(answer)
    
others_solution()


# 16분 문제 이해 잘못함,,,,, 연속적이어야 하는줄
'''

N = int(input())
A = [-1]+list(map(int,input().split())) # 수열

# dp[i][j] = 왼쪽에서부터 i번째까지 탐색했을 때, i가 제일 큰 경우의 길이
# dp = [ [0]*N for _ in range(N) ]
dp = [0]*(N+1)
for i in range(1,N+1):
    print("i=",i)
    if A[i]>A[i-1]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = 1
print("A=",A)
print("dp=",dp)

# dp2[i][j] = 오른쪽에서부터 j번째까지 탐색했을 때, j가 제일 큰 경우의 길이
# dp2 = [ [0]*N for _ in range(N) ]
dp2 = [0]*(N+1)
dp2[-1]=1
for j in range(N-1,0,-1):
    print("j=",j)
    if A[j]>A[j+1]:
        dp[j] = dp[j+1]+1
    else:
        dp[j] = 1
print("A=",A)
print("dp2=",dp)
'''