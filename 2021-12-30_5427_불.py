''' 
1. board에 불,상근 도착시간 쓰면 typeerror
   (board가 숫자,# 섞이기 때문에)
   fdist,sdist로 따로 관리하는 게 나음
2. 시간초과 -> 이미 방문한 칸 다시 방문하지 않도록 !
'''

import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
    
def bfs(q): 
    
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            # 탈출했으면
            if nx<0 or nx>=h or ny<0 or ny>=w: 
                return sdist[x][y]+1 
            # 이미 방문한 칸이거나 벽이면
            if sdist[nx][ny]>=0 or board[nx][ny]=='#': continue 
            # 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸이면
            if fdist[nx][ny]!=-1 and fdist[nx][ny]<=sdist[x][y]+1: continue 
            sdist[nx][ny]=sdist[x][y]+1
            q.append((nx,ny))
            
    return "IMPOSSIBLE"         

for _ in range(int(input())):
    w,h = map(int,input().split())
    board = []
    for _ in range(h):
        board.append(list(input().rstrip()))
        '''
        '.': 빈 공간
        '#': 벽
        '@': 상근이의 시작 위치
        '*': 불
        '''
    q1 = deque() # 불
    q2 = deque() # 상근
    fdist = [ [-1]*w for _ in range(h) ]
    sdist = [ [-1]*w for _ in range(h) ]

    for r in range(h):
        for c in range(w):
            if board[r][c]=='*': # 불
                q1.append((r,c))
                fdist[r][c]=0
            elif board[r][c]=='@': # 상근
                q2.append((r,c))
                sdist[r][c]=0
            
    # 불 전파
    while q1:
        x,y = q1.popleft()
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if nx<0 or nx>=h or ny<0 or ny>=w: continue
            # 이미 방문한 칸이거나 벽이면
            if fdist[nx][ny]>=0 or board[nx][ny]=='#': continue 
            fdist[nx][ny]=fdist[x][y]+1
            q1.append((nx,ny))
    
    # 상근 달리기
    print(bfs(q2))
         