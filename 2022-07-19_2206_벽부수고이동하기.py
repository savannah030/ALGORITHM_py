# 21분 혹시나 돌려봤으나 실패
# 28분 ok
# bfs는 최단 거리로 탐색하므로 한번 방문하면 또 방문할 필요없음
# 따라서 dist[nx][ny][broken]>dist[x][y]+1 쓸 필요없이 dist[nx][ny][broken]==-1 쓰면 됨!!
import sys
input = sys.stdin.readline
from collections import deque
INF = int(10e9)+1

N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().rstrip())))
dist = [ [[-1]*2 for _ in range(M)] for _ in range(N) ] # dist[x][y][broken]

# bfs
dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
q.append((0,0,0))
dist[0][0][0]=1
while q:
    x,y,broken = q.popleft()
    if x==N-1 and y==M-1:
        print(dist[x][y][broken])
        exit(0)
    for dir in range(4):
        nx,ny = x+dx[dir],y+dy[dir]
        if nx<0 or nx>=N or ny<0 or ny>=M: continue
        # 벽인데
        if board[nx][ny]==1:
            # 아직 부순 적 없으면
            if broken==0 and dist[nx][ny][broken+1]==-1: 
                dist[nx][ny][broken+1] = dist[x][y][broken]+1
                q.append((nx,ny,broken+1))
        # 갈 수 있는 칸이고
        elif board[nx][ny]==0 and dist[nx][ny][broken]==-1:
            # 최솟값으로 갱신
            dist[nx][ny][broken] = dist[x][y][broken]+1
            q.append((nx,ny,broken))
print(-1)

            
        
