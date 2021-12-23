# 47분 구현중..
# +30분 경우의 수 세는 거 어려워... 프로그래머스 64064 불량사용자 오마주
# +21분
# +52분 디버깅 계속
import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 1<=세로,가로<=8
board = [] # 0=빈칸, 6=벽, 1~5=CCTV종류, cctv 개수 8개 이하
for _ in range(N):
    board.append(list(map(int,input().split()))) 
'''
cctvs
cctv = [[(0, 1), (2, 1)], [(1, 2), (1, 3), (1, 4), (1, 5), (1, 0)]] # # cctv가 회전할때마다 감시하는 영역의 좌표들로 배열을 만듦(2차원배열) 
cctv = [[(4, 4), (5, 4)], [(3, 5), (3, 3), (3, 2)]]
cctv = [ [(4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)] ]
'''
cctvs = [] 

dx = [-1,0,1,0] # 북동남서(90도씩 회전)
dy = [0,1,0,-1]
for i in range(N):
    for j in range(M):
        if board[i][j]==0 or board[i][j]==6: continue
        
        elif board[i][j]==1:
            cctv = [ [] for _ in range(4) ]
            for dir in range(4):
                x,y = i,j #######
                while True:
                    nx,ny = x+dx[dir],y+dy[dir]
                    if nx<0 or nx>=N or ny<0 or ny>=M: break
                    if board[nx][ny]==6: break
                    cctv[dir].append((nx,ny))
                    x,y = nx,ny #######
                    
        elif board[i][j]==2:
            cctv = [ [] for _ in range(2) ]
            for dir in range(2):
                for d in [dir,(dir+2)%4]:
                    x,y = i,j
                    while True:
                        nx,ny = x+dx[d],y+dy[d]
                        if nx<0 or nx>=N or ny<0 or ny>=M: break
                        if board[nx][ny]==6: break
                        cctv[dir].append((nx,ny))
                        x,y = nx,ny
                        
        elif board[i][j]==3:
            cctv = [ [] for _ in range(4) ]
            for dir in range(4):
                for d in [dir,(dir+1)%4]:
                    x,y = i,j
                    while True:
                        nx,ny = x+dx[d],y+dy[d]
                        if nx<0 or nx>=N or ny<0 or ny>=M: break
                        if board[nx][ny]==6: break
                        cctv[dir].append((nx,ny))
                        x,y = nx,ny
                        
        elif board[i][j]==4: 
            cctv = [ [] for _ in range(4) ]
            for dir in range(4):
                for d in [dir,(dir+1)%4,(dir+2)%4]: 
                    x,y = i,j
                    while True:
                        nx,ny = x+dx[d],y+dy[d]
                        if nx<0 or nx>=N or ny<0 or ny>=M: break
                        if board[nx][ny]==6: break
                        cctv[dir].append((nx,ny))
                        x,y = nx,ny
             
        elif board[i][j]==5:
            cctv = [ [] ]
            for dir in range(4):
                x,y = i,j
                while True:
                    nx,ny = x+dx[dir],y+dy[dir]
                    if nx<0 or nx>=N or ny<0 or ny>=M: break
                    if board[nx][ny]==6: break
                    cctv[0].append((nx,ny))
                    x,y = nx,ny
              
        ############ (x,y) 없으면 아예 cctvs에 넣지않음 (이따 len(cctvs[k])에서 indexerror 나지 않게 하기 위함)         
        for c in cctv: 
            if len(c)!=0: 
                cctvs.append(cctv)
                break
        
'''
cctvs
cctv = [[(0, 1), (2, 1)], [(1, 2), (1, 3), (1, 4), (1, 5), (1, 0)]] # # cctv가 회전할때마다 감시하는 영역의 좌표들로 배열을 만듦(2차원배열) 
cctv = [[(4, 4), (5, 4)], [(3, 5), (3, 3), (3, 2)]]
cctv = [ [(4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)] ]
'''
# 각 cctvs[i]마다 경우 하나씩 뽑기(dfs탐색)
def dfs(k,board):
    
    global ans
    
    if k==len(cctvs):
        
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j]==0: ######## 벽은 사각지대일 수 없음
                    cnt += 1
        ans = min(ans,cnt)
        return 
    
    for case in range(len(cctvs[k])):
        newboard = [board[i][:] for i in range(N)] # 기존 board값 복사
        for (x,y) in cctvs[k][case]:
            newboard[x][y]='#'
        dfs(k+1,newboard)

ans = 100
if len(cctvs)==0:
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]==0:
                cnt += 1
    print(cnt)
else:
    for _ in range(len(cctvs[0])):     
        dfs(0,[board[i][:] for i in range(N)])
        
    print(ans)


        
        
    

   
    
    
    
    