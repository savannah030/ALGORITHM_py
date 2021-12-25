# 삽질했음.. 큐에 뿌요들 한번에 넣는게 아님!
# 뿌요 하나 넣고 큐 돌면서 같은 뿌요들 좌표 puyos 배열에 추가
import sys
input = sys.stdin.readline
from collections import deque

board = []
for _ in range(12):
    board.append(list(input().rstrip()))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def pop_and_fall(pts_li,board):
    
    # pop
    for pts in pts_li:
        for pt in pts:
            board[pt[0]][pt[1]]='.'
            
    # fall
    for y in range(6):
        for x in range(11,-1,-1):
            if board[x][y]=='.': continue
            idx = x
            while idx<11 and board[idx+1][y]=='.':
                idx += 1
            if idx!=x:
                board[idx][y]=board[x][y]
                board[x][y]='.'  

    return board
                

ans = 0       
while True:
    
    q = deque()
    visited = [ [False]*6 for _ in range(12) ]
    burst = [] 
    for i in range(12):
        for j in range(6):
            
            if board[i][j]=='.': 
                visited[i][j]=True 
                continue
            
            if visited[i][j]: continue
            
            q.append((i,j)) 
            visited[i][j]=True
            puyos=[(i,j)]
            color = board[i][j]
            
            # 인접한 같은색 뿌요들의 좌표 bfs 탐색
            while q:
                x,y = q.popleft()
                for dir in range(4):
                    nx,ny = x+dx[dir],y+dy[dir]
                    if nx<0 or nx>=12 or ny<0 or ny>=6: continue
                    if visited[nx][ny]: continue
                    if board[nx][ny]==color:
                        q.append((nx,ny))  
                        visited[nx][ny]=True
                        puyos.append((nx,ny))
              
            # 4개 이상일 때에만 burst에 넣음       
            if len(puyos)>=4:   
                burst.append(puyos)
          
    # 더이상 없어질 뿌요가 없으면
    if len(burst)==0: 
        print(ans)
        break
    ans += 1
    board = pop_and_fall(burst,board)
            
    