# 25분 2%에서 틀렸습니다,,,
# 32분 79%에서 메모리 초과,,,
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(node):
    
    global answer
    visited[node]=True
    cycle.append(node)
    nxt = graph[node]
    
    if visited[nxt]:
        if nxt in cycle:
            answer -= (len(cycle)-cycle.index(nxt)) 
            return
        
    if not visited[nxt]:
        dfs(nxt)

for _ in range(int(input())): # 테스트케이스
    n = int(input())
    graph = [-1]+list(map(int,input().split()))
    visited = [False]*(n+1) # 1번부터 시작
    answer = n
    for x in range(1,n+1):
        if not visited[x]:
            cycle = []
            dfs(x)
    print(answer)