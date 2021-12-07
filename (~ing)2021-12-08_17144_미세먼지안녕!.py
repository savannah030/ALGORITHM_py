### 인덱스 범위 생각하는데 오래걸림 
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 
# 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())  #6 ≤ R, C ≤ 50, 1 ≤ T초 ≤ 1,000
board = []
for _ in range(R):
    board.append(list(map(int,input().split())))
'''
print("newboard")
for r in range(R):
    print(newboard[r])
'''
for r in range(R):
    if board[r][0]==-1:
        above,below = r,r+1
        board[above][0]=0
        board[below][0]=0
        break

newboard = [board[r][:] for r in range(R)]
   
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for t in range(T):
 
    # 미세먼지 확산
    for r in range(R):
        for c in range(C):
            if (r==above and c==0) or (r==below and c==0): continue
            k = board[r][c]//5
            for dir in range(4):
                nx = r+dx[dir]
                ny = c+dy[dir]
                if nx<0 or nx>=R or ny<0 or ny>=C: continue
                if (nx==above and ny==0) or (nx==below and ny==0): continue
                newboard[nx][ny] += k
                newboard[r][c] -= k
    '''      
    print("미세먼지",t)
    for r in range(R):
        print(newboard[r])
    '''
    # 위쪽 공기청정기 작동
    for r in range(above,0,-1):       
        newboard[r][0] = newboard[r-1][0] 
    newboard[above][0]=0 #####
    for c in range(C-1):          
        newboard[0][c] = newboard[0][c+1]
    for r in range(above):
        newboard[r][C-1] = newboard[r+1][C-1]
    for c in range(C-1,0,-1):
        newboard[above][c] = newboard[above][c-1]
    
    # 아래쪽 공기청정기 작동
    for r in range(below,R-1):
        newboard[r][0] = newboard[r+1][0]
    newboard[below][0]=0 #####
    for c in range(C-1):
        newboard[R-1][c] = newboard[R-1][c+1]
    for r in range(R-1,below,-1):
        newboard[r][C-1] = newboard[r-1][C-1]
    for c in range(C-1,0,-1):
        newboard[below][c] = newboard[below][c-1]
    
    '''
    print("공기청정기",t)
    for r in range(R):
        print(newboard[r])
    '''
    board = [newboard[r][:] for r in range(R)]
    
print(sum(map(sum,newboard)))