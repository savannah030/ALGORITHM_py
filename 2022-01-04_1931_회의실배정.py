# 1.끝나는 시간 2.시작하는 시간 순으로 정렬
# 끝나는 시간이 빠른 게 무조건 유리

import sys
input = sys.stdin.readline

info = []
N = int(input())
for _ in range(N):
    info.append(tuple(map(int,input().split())))
info = sorted(info, key=lambda x:(x[1],x[0]))

ans = 0
end = 0
for n in range(N):
    if info[n][0]>=end:
        ans += 1
        end = info[n][1]
        
print(ans)

