import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())# 세로,가로

# '맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다'는 조건 안봐서 가장자리에 0 추가함
board = []
board.append([0]*(M+2))
for _ in range(N):
    board.append([0]+list(map(int,input().split()))+[0])
board.append([0]*(M+2))

def oneHourLater(i,j):  # bfs
    visited = [ [False]*(M+2) for _ in range(N+2)]
    edge = deque() # 가장자리 치즈
    q = deque()
    q.append((i,j))
    visited[i][j]=True
    
    while q:
        x,y = q.popleft()
        for (nx,ny) in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if nx<0 or nx>=(N+2) or ny<0 or ny>=(M+2): continue
            if visited[nx][ny]: continue
            if board[nx][ny]==0:
                q.append((nx,ny))
            if board[nx][ny]==1:
                edge.append((nx,ny))
            visited[nx][ny]=True
    #print("edge=",edge) 
      
    melt = []
    for e in edge: # 한꺼번에 확인
        x,y = e
        cnt = 0
        for (nx,ny) in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if nx<0 or nx>=(N+2) or ny<0 or ny>=(M+2): continue   
            if board[nx][ny]==0 and visited[nx][ny]:  #########
                cnt += 1
        if cnt>=2:
            melt.append((x,y)) # 여기서 바로 board[x][y]=0 하면 같은 시간의 치즈에 영향을 미침
    
    for m in melt: # 한꺼번에 확인
        board[m[0]][m[1]]=0
            
    return board

time = 0
while True:
    time += 1
    board = oneHourLater(0,0)
    '''
    print("time=",time)
    for i in range(N+2):
        print(" ".join(map(str,board[i])))
    '''
    if sum(map(sum,board))==0:
        print(time)
        break

