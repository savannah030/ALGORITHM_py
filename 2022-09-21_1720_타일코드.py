# 14분 3%에서 틀렸습니다,,
# 17분 98%에서 틀렸습니다,,
# 23분 N==1,2일 때 수작업
import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
dp[1]=1
if N>=2: dp[2]=3
for n in range(3,N+1):
    dp[n] = dp[n-2]*2+dp[n-1]

if N==1:
    symmetry = 1
elif N==2:
    symmetry = 3
elif N%2==0:   
    symmetry = dp[N//2-1]*2+dp[N//2]
else:
    symmetry = dp[N//2]
print(symmetry+(dp[N]-symmetry)//2) 