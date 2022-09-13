import sys
input = sys.stdin.readline
# 지나가는 방의 개수는 무조건 육각형 테두리 개수
N = int(input())
INF = int(10e9)+1
for n in range(1,INF):
    if N<=3*n*(n-1)+1:
        print(n)
        break