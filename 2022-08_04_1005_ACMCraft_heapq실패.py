# 33분 테스트케이스는 다맞음 8% 시간초과,,
# 최장경로는 다익스트라로 못품..
import sys
input = sys.stdin.readline
from heapq import heappush,heappop

for _ in range(int(input())): # 테스트케이스 수
    
    N,K = map(int,input().split()) # 건물의개수,건설순서규칙
    weights = [-1]+list(map(int,input().split())) # 각 건물당 건설에 걸리는 시간 
    graph = [ [] for _ in range(N+1) ] # 1번부터 시작
    cnt = [0]*(N+1)
    
    for _ in range(K):
        X,Y = map(int,input().split())
        #graph[X].append(Y)
        graph[Y].append(X) # 도착지부터 탐색할거기 때문에 화살표 반대방향 정보넣기
        cnt[Y] += 1
    #print("cnt=",cnt)
    end = int(input())
    q = []
    heappush(q,(-weights[end],end)) # 도착지부터 최대다익스트라
    dist = [-1]*(N+1)
    dist[end]=weights[end]
    ### 다익스트라는 출발지 하나 얘는 도착지 하나
    answer = 0
    while q:
        weight,node = heappop(q)
        #print("node=",node)
        weight = -weight
        if weight<dist[node]: continue
        if cnt[node]==0:
            answer = max(answer,dist[node])
        for prev in graph[node]:
            distance = weight+weights[prev] # end~node~prev(node 거쳐서 가는 경로)
            if dist[prev]<distance:
                dist[prev]=distance
                heappush(q,(-distance,prev))
                
    #print("dist=",dist)
                
    '''
    for node in range(1,N+1):
        if cnt[node]==0:
            answer = max(answer,dist[node])
    '''       
    print("answer=",answer,end="\n\n") 