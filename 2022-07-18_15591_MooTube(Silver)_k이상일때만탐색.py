####  너무 많은 동영상이 추천되면 소들이 일하는 것이 방해될까 봐 걱정하고 있다! 그래서 그는 K를 적절한 값으로 결정하려고 한다.
### 요게 포인트 !!
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
        node,USADO = q.popleft() # USADO = node까지 가는 경로 중 최솟값
        for (nxt,nxt_cost) in graph[node]:
            nxt_USADO = min(USADO,nxt_cost)
            # 가는 경로 중 최솟값이 유사도이기 때문에 nxt_cost가 k 이상인 경우만 보면 됨
            # k 미만인 경우는 유사도가 k 미만인 값이 되어버리니까
            if nxt_USADO>=k and not visited[nxt]:
                answer += 1
                visited[nxt]=True
                q.append((nxt,nxt_USADO))
                    
    print(answer)
