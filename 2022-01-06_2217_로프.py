import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort(reverse=True)

# 로프 i개를 쓸 때 들 수 있는 최대 중량은 ropes[i-1]*i
print(max([ropes[i]*(i+1) for i in range(N)]))

