# dfs 함수 진입했을 때 물고기 먹으면 진입 전후로 board 상태 되돌릴 필요없음
# board, pos 다 deepcopy하기 때문에 dfs문 서로에게 영향주지않음
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
        #if n==99: break ###########
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

def fishMove2(_board,_info):
  
    nums = sorted(_info.keys())
    for n in nums:
        #if n==99: break
        x,y = _info[n]
        dir = _board[x][y][1]
        for i in range(8):
            ndir = (dir+i)%8
            nx,ny = x+dx[ndir],y+dy[ndir]
            if nx<0 or nx>=4 or ny<0 or ny>=4: continue

            if _board[nx][ny][0]!=99: 
                _board[x][y][1]=ndir
                _info[n]=(nx,ny)
                if _board[nx][ny][0]!=-1:
                    _info[_board[nx][ny][0]]=(x,y)
                _board[x][y],_board[nx][ny] = _board[nx][ny],_board[x][y]
                break  
        else:
            _board[x][y][1] = dir
            
      
    return _board,_info

def dfs(r,c,cnt,board,pos): 
    
    global ans
    # 상어가 (r,c) 물고기 먹음
    # # dfs 함수 진입했을 때 물고기 먹으면 진입 전후로 board 상태 되돌릴 필요없음
    eatten = board[r][c][:]
    cnt += board[r][c][0]
    del pos[eatten[0]] 
    board[r][c] = [99,eatten[1]]
    
    ans = max(ans,cnt) ##########

    # fish move
    newboard,newpos = fishMove2(board,pos) 
    
    # shark moves
    d = newboard[r][c][1]
    for n in range(1,4):
        nr = r+dx[d]*n
        nc = c+dy[d]*n
        if nr<0 or nr>=4 or nc<0 or nc>=4: break
        
        if newboard[nr][nc][0]!=-1: ##### 갈곳이 없으면 재귀 끝 !
            newboard[r][c]=[-1,-1]  # 상어가 있던 자리 비우기
            # board, pos 다 deepcopy하기 때문에 dfs문 서로에게 영향주지않음
            dfs(nr,nc,cnt,deepcopy(newboard),deepcopy(newpos))
 
ans = 0
dfs(0,0,0,deepcopy(board),deepcopy(pos))
print(ans)




        



