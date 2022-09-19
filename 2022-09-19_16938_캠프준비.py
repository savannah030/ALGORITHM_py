# 15분
import sys
input = sys.stdin.readline

# 문제수, L<=난이도합<=R, 난이도차>=X
N, L, R, X = map(int,input().split())
problems = list(map(int,input().split()))
vis = [False]* (1 << N)
answer = 0

def backtracking(idx, selected_problems, state):
    
    global answer
    
    if vis[state]: return
    vis[state] = True
    
    if len(selected_problems)>=2 and L<=sum(selected_problems)<=R and max(selected_problems)-min(selected_problems)>=X:
        #print("hi=",selected_problems,bin(state)[2:].zfill(N))
        answer += 1
    
    for i in range(idx,N):
        backtracking(i+1, selected_problems[:]+[problems[i]], state|(1<<i))
  

backtracking(0, [], 0)
print(answer)
