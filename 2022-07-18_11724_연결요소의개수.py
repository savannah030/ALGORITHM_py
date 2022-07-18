#14분
import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split()) # 정점개수,간선개수
graph = [[] for _ in range(N+1)] # 1번부터 시작
visited = [False]*(N+1)

# 인접 리스트
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0  
for x in range(1,N+1):
    if not visited[x]:
        # bfs
        answer += 1
        visited[x] = True
        q = deque()
        q.append(x)
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
print(answer)
               
                    
        
        
    
    
    