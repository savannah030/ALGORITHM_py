# 20분
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

dp = [1]*N # dp[i] = A[:i+1]의 가장 긴 증가하는 부분수열의 길이
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if A[i]>A[j]:
            dp[i] = max(dp[i],dp[j]+1)
l = max(dp)
print(l)
# 역순으로 탐색해야함
# 순차적으로 탐색하는 경우 반례:
# A = [1,5,6,2,3,4,7]
# dp= [1,2,3,2,3,4,5]
# answer = 1 5 6 4 7 되어버림
answer = []
i,value = N-1,l
while value>=0 and i>=0:
    if dp[i]==value:
        answer.append(A[i])
        value -= 1
    i -= 1
for a in answer[::-1]:
    print(a,end=' ')

        
    
    