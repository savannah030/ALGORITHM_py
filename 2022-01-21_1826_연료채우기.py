import sys
input = sys.stdin.readline
from heapq import heappush,heappop

N = int(input()) #  주유소의 개수 N(1 ≤ N ≤ 10,000)
stations = []
for _ in range(N):
    a,b = map(int,input().split()) # 1 ≤ 시작 위치~주유소 거리 ≤ 1,000,000, 1 ≤ 주유소에서 채울수있는 연료의 양 ≤ 100
    stations.append((a,b))
stations.sort()
L,P = map(int,input().split()) # 1 ≤ 성경~마을 거리 ≤ 1,000,000, 1 ≤ 트럭에있던 연료의 양 ≤ 100
stations.append((L,0))

pos = 0
remain = P
reserve = []
ans = 0
for (dist,fuel) in stations:
    remain -= dist-pos
    while remain<0:
        if not reserve: print(-1); exit(0)
        remain += -heappop(reserve)
        ans += 1
    heappush(reserve, -fuel) # 현재 도달 가능한 주유소를 힙에 넣음
    pos = dist
print(ans)
    