# 2시간 반?+46분
# 1. 50 2. keyError(line 81 del newpos[eatten[0]]) 3. 35 4. 19
# https://hello-i-t.tistory.com/56
import sys
input = sys.stdin.readline
from copy import deepcopy

board = [ [ [0,0] for _ in range(4)] for _ in range(4) ]
pos = dict()
for i in range(4):
    li = list(map(int,input().split()))
    for j in range(4):
        board[i][j][0] = li[2*j]  # 물고기번호 
        board[i][j][1] = li[2*j+1]-1 # 방향
        pos[li[2*j]] = (i,j) #pos[번호]=(x,y)
         
dx = [-1,-1,0,1,1,1,0,-1] # ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
dy = [0,-1,-1,-1,0,1,1,1]

def fishMove(board,pos):
    nums = sorted(pos.keys())
    for n in nums: 
        if n==99: break ###########3
        x,y = pos.get(n)   
        d = board[x][y][1]
        # 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
        # 이동할 수 없는 경우:  상어가 있거나, 공간의 경계를 넘는 칸
        cnt = 0
        while (x+dx[d]<0 or x+dx[d]>=4 or y+dy[d]<0 or y+dy[d]>=4) or board[x+dx[d]][y+dy[d]][0]==99: # 이게 최선입니까
            d = (d+1)%8
            cnt += 1
            if cnt==8: break
        if cnt==8:
            nx,ny = x,y
        else:
            nx,ny = x+dx[d],y+dy[d]
            board[x][y][1]=d ##########
            pos[board[x][y][0]] = (nx,ny)
            if board[nx][ny][0]!=-1: ################
                pos[board[nx][ny][0]] = (x,y) 
            board[x][y],board[nx][ny] = board[nx][ny],board[x][y] 
    return board,pos

def dfs(r,c,cnt,board,pos): 
    
    global ans
    # 상어가 (r,c) 물고기 먹음
    eatten = board[r][c][:]
    cnt += board[r][c][0]
    del pos[eatten[0]] 
    board[r][c] = [99,eatten[1]]

    # fish move
    newboard,newpos = fishMove(board,pos) 
    
    ans = max(ans,cnt) ##########
    
    # shark moves
    d = newboard[r][c][1]
    flag = False
    for n in range(1,4):
        nr = r+dx[d]*n
        nc = c+dy[d]*n
        if nr<0 or nr>=4 or nc<0 or nc>=4: break
        
        if newboard[nr][nc][0]!=-1: ##### 갈곳이 없으면 재귀 끝 !
            newboard[r][c]=[-1,-1]
            dfs(nr,nc,cnt,deepcopy(newboard),deepcopy(newpos))
 
ans = 0
dfs(0,0,0,deepcopy(board),deepcopy(pos))
print(ans)




        



