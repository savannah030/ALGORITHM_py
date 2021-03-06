# 브루트 포스
# 사다리 놓을 수 없는 경우는 old+new 합쳐서 확인! (new만 확인하면 안됨.)
import sys
from itertools import combinations
input = sys.stdin.readline

N,M,H = map(int,input().split()) 

graph = [[False]*N for _ in range(H)] #(h,n) 
old = []
for _ in range(M):
    a,b =  map(int,input().split()) # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미
    graph[a-1][b-1]=True
    old.append((a-1,b-1))
    
cand = []  
for i in range(H):
    for j in range(N-1): #### 마지막 세로선에서 오른쪽으로 뻗을 수 있는 가로선은 없음
        if graph[i][j]: continue
        if j==0 and graph[i][j+1]: continue
        if 0<j<N-1 and graph[i][j-1] and graph[i][j+1]: continue
        cand.append((i,j))

def start():
    for y in range(N):
        now = y
        for x in range(H):
            if now<N-1 and graph[x][now]: ##### now+1 아님!!!!!
                now += 1
            elif now>0 and graph[x][now-1]: 
                now -= 1
        if now!=y: return False
    return True

for n in range(4):
    for ladders in combinations(cand,n): #ladders(이번 for문에서 사다리를 놓을 위치) #ladders= [(3, 2), (5, 2), (5, 4)] 
        for (x,y) in ladders:            
            graph[x][y]=True
        if start():
            print(len(ladders))
            sys.exit(0)
        for (x,y) in ladders:
            graph[x][y]=False #백트래킹
print(-1)

    