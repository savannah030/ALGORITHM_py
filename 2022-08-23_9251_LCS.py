import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

dp = [ [0]*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
      
print(dp[-1][-1])

# 21분
'''
value = 0
j_idx = 0
dp = [ [-1]*(len(s2)) for _ in range(len(s1))]
# break하지말고 완전 탐색해야함(예 s1=AAAA, s2=AA이면 dp[-1][-1]까지 가지 못함)
for i in range(len(s1)):
    for j in range(j_idx,len(s2)):
        dp[i][j]=value
        if s1[i]==s2[j]:
            if j-1>=0:
                dp[i][j] = dp[i][j-1]+1
            else:
                dp[i][j] = 1
            value = dp[i][j]
            j_idx = j
            break
      
for i in range(len(s1)):
    print(dp[i])
print(value)
'''
    
            
            

