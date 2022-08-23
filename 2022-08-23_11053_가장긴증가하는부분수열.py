import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

dp = [1]*N # dp[i] = A[:i+1]의 가장 긴 증가하는 부분수열의 길이
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if A[i]>A[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp)) 
        
    