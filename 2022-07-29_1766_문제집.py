import sys
input = sys.stdin.readline
from heapq import heappush,heappop

# 가능하면 쉬운 문제(문제번호가 작은)부터 풀어야 하기 때문에 deque 대신 heapq 사용 !!

N,M = map(int,input().split()) #문제수,정보개수
graph = [ [] for _ in range(N+1)] # 1번부터 시작
inDegree = [0]*(N+1)
for _ in range(M):
    A,B = map(int,input().split()) 
    graph[A].append(B) #A번 문제는 B번 문제보다 먼저 푸는 것이 좋다
    inDegree[B] += 1
graph = [sorted(g) for g in graph]
    
q = []
for i in range(1,N+1):
    if inDegree[i]==0:
        heappush(q,i)
    
while q:
    node = heappop(q)
    print(node,end=' ')
    for nxt in graph[node]:
        inDegree[nxt] -= 1
        if inDegree[nxt]==0:
            heappush(q,nxt)