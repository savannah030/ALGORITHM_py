import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) # 1<=세로,가로<=20
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

coins = []
for n in range(N):
    for m in range(M):
        if board[n][m]=='o':
            coins.append((n,m))
   
dx = [0,0,1,-1]
dy = [1,-1,0,0]     

def bfs():
    
    global answer
    q = deque()
    x1,y1 = coins[0]
    x2,y2 = coins[1]
    q.append((x1,y1,x2,y2,1))
    # visited는 dropped==0일때만(두 동전이 모두 보드에 있을때만) 관리함 
    visited = [ [[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N) ] 
    visited[x1][y1][x2][y2]=True
    while q:
        x1,y1,x2,y2,cnt = q.popleft()
        if cnt>answer or cnt>10: break
        
        for dir in range(4):
            dropped = 0
            nx1,ny1,nx2,ny2 = x1+dx[dir],y1+dy[dir],x2+dx[dir],y2+dy[dir]
          
            # 2. 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
            if nx1<0 or nx1>=N or ny1<0 or ny1>=M: dropped += 1 
            if nx2<0 or nx2>=N or ny2<0 or ny2>=M: dropped += 1    
            
            if dropped==2:
                continue
            if dropped==1:
                answer = min(answer,cnt)
            if dropped==0: 
                # 1. 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
                if board[nx1][ny1]=='#': nx1,ny1 = x1,y1
                if board[nx2][ny2]=='#': nx2,ny2 = x2,y2
                if not visited[nx1][ny1][nx2][ny2]:
                    visited[nx1][ny1][nx2][ny2]=True
                    q.append((nx1,ny1,nx2,ny2,cnt+1))

answer = 11
bfs()
if answer==11:
    print(-1)
else:
    print(answer)



