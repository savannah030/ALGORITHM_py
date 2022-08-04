import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = int(10e9)+1
# C = 0인 경우는 순간 이동을 하는 경우, 
# C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우
# 사이클(음의간선) 이 발생하면 -1 -> 벨만포드
# 경로가 없어도 -1

N,M = map(int,input().split()) # 도시,버스
graph = [] # 1번부터 시작
for _ in range(M):
    graph.append(list(map(int,input().split()))) # A,B,C
    
    

q = [(0,1)] #(node까지의cost,node)
dist = [INF]*(N+1)
dist[1]=0

for round in range(N):
    for (st,en,cost) in graph:
        # cost가 음수일 수 있으므로, dist[st]!=INF 꼭 확인해야함!
        if dist[st]!=INF and dist[en]>dist[st]+cost:
            # 마지막 라운드에서도 갱신된다는 것은, 음의 사이클 존재한다는 것!
            if round == N-1:
                print(-1)
                exit(0)
            dist[en]=dist[st]+cost
            
for node in range(2,N+1):
    if dist[node]==INF:
        print(-1)
    else:
        print(dist[node])
            