# 21분 8%에서 틀렸습니다
# 58%에서 틀렸습니다
# 각 depth마다 건설 시간이 가장 긴 건물의 건설 시간을 더하는 것이 최소 건설 시간을 보장하지 않음 !!
# 경로 중 건설시간 가장 긴 거 골라야함 !!
# https://www.acmicpc.net/board/view/30959 다익스트라는 최장경로에 쓸 수 없음

import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())): # 테스트케이스 수
    N,K = map(int,input().split()) #건물개수, 규칙개수
    graph = [ [] for _ in range(N+1)] # 방향 그래프
    weight = [-1]+list(map(int,input().split())) # 1번부터 시작
    indegree = [0]*(N+1)
    for _ in range(K):
        X,Y = map(int,input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    q = deque()
    dp = [0]*(N+1)
    for i in range(1,N+1): # 진입차수가 0인 노드 여러개일 수 있음
        if indegree[i]==0:
            q.append(i) #(node,weight)   
            dp[i]=weight[i]

    while q: 
        # now는 건설 시작할 수 있는 노드
        # 그 전 건물들이 모두 지어진 상태
        now = q.popleft()
        for nxt in graph[now]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt],dp[now]+weight[nxt])
            if indegree[nxt]==0:
                q.append(nxt)
                
    print(dp[int(input())])
            
    
    
    
        