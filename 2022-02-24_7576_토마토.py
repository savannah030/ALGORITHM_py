import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1];
dy = [1,-1,0,0];

M,N = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

# bfs
q = deque()
for n in range(N):
    for m in range(M):
        if board[n][m]==1:
            q.append((n,m))
            
while q:
    x,y = q.popleft()            
    for dir in range(4):
        nx = x+dx[dir]
        ny = y+dy[dir]
        if nx<0 or nx>=N or ny<0 or ny>=M: continue
        if board[nx][ny]: continue # 토마토가 들어있지 않거나 이미 익은 토마토가 들어있으면
        board[nx][ny]=board[x][y]+1
        q.append((nx,ny))

def start():
    for x in range(N):
        for y in range(M):
            if board[x][y]==0:
                return -1
    return max(map(max,board))-1

print(start())
                
