# 깊이 하나씩 들어갈 때마다 MIN 갱신 <-- xxx 이거 아닌 것 같은데..
# 27분

import sys
input = sys.stdin.readline
from collections import deque
INF = int(10e9)+1

N,Q = map(int,input().split())
graph = [ [] for _ in range(N+1) ] # 1번부터 시작
for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))
    
for i in range(Q):
    # 동영상 v에 대해 유사도가 k이상인 동영상의 개수를 찾기
    k,v = map(int,input().split()) 
    visited = [False]*(N+1)
    answer = 0
    
    q = deque()
    visited[v] = True
    q.append((v,INF))
    while q:
        node,node_cost = q.popleft() # node_cost는 node에서의 USADO(가는 경로 중 최솟값)
        # node의 USADO가 k이상이면
        if node_cost!=INF and node_cost>=k: answer += 1
        for (nxt,nxt_cost) in graph[node]:
            if not visited[nxt]:
                visited[nxt]=True
                if nxt_cost<node_cost:
                    q.append((nxt,nxt_cost)) 
                else:
                    q.append((nxt,node_cost)) 
                    
    print(answer)
    
'''
for i in range(Q):
    # 동영상 v에 대해 유사도가 k이상인 동영상의 개수를 찾기
    k,v = map(int,input().split()) 
    visited = [False]*(N+1)
    answer = 0
    
    q = deque()
    visited[v] = True
    q.append((v,INF))
    while q:
        node,MIN = q.popleft()
        for (nxt,cost) in graph[node]:
            if not visited[nxt]:
                visited[nxt]=True
                if cost<MIN:
                    q.append((nxt,cost))
'''                  
                    
        
        
    