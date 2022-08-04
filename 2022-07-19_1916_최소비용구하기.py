import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = int(10e9)+1

N = int(input()) # city
M = int(input()) # bus

graph = [ [] for _ in range(N+1)]
for _ in range(M):
    u,v,cost = map(int,input().split())
    graph[u].append((cost,v))
   
    
def dijkstra(st,en):
    q = []
    heappush(q,(0,st)) # (cost,node)
    dist = [INF]*(N+1)
    dist[st]=0

    while q:
        cost,node = heappop(q)
        if cost>dist[node]: continue
        if node==en:
            return dist[en]
        for (nxt_cost,nxt_node) in graph[node]:
            tmp_cost = cost+nxt_cost
            if tmp_cost<dist[nxt_node]:
                dist[nxt_node]=tmp_cost
                heappush(q,(tmp_cost,nxt_node))
                
st,en = map(int,input().split())
print(dijkstra(st,en))