# 1:18 시작하자마자 틀렸습니다. 테스트케이스는 다 맞는데.. 문제에서 빼먹은 조건이 있는듯
# 1:51 연속으로 없애는 거 구현해야함! -> 성공
import sys
input = sys.stdin.readline

N = int(input()) # 1<=블록을 놓은 횟수<=10,000
board1 = [ [False]*4 for _ in range(10)] # Red & Green
board2 = [ [False]*4 for _ in range(10)] # Red & Blue ###### rotate 시키기
score = 0

##### 54분 2X1인 경우 생각못함
def drop(pts,board): 
    global score
    
    
    # while문 -> nx값 +1씩 갱신
    # 범위 벗어나거나 해당 칸에 타일 있으면 check=False돼서 다음 while문 돌지 않음 
    check = True
    while check: 
        for pt in pts:
            nx,ny = pt[0]+1,pt[1]
            if nx>=10: 
                check=False
                break
            if board[nx][ny]: 
                check=False
                break
        else:
            for i in range(len(pts)):
                pts[i][0] += 1
                
    # nx칸으로 타일 옮기기         
    for pt in pts:
        board[pt[0]][pt[1]]=True
    
    # 밑에 while문에서 쓸 함수. 없애야할 줄이 있는지 확인하고 idx 리턴 없으면 -1 리턴
    def check():
        for x in range(9,0,-1):
            for y in range(4):
                if not board[x][y]: 
                    break
            else: ## x행 다 True면
                return x
        return -1
    
    # 한줄 없애고 점수얻기 ######### 연속으로 없애는 거 구현해야함
    while True:
        start = check() 
        if start==-1: break
        for x in range(start,0,-1):
            for y in range(4):
                if not board[x][y]: 
                    break
            else: ## x행 다 True면
                score += 1
                for r in range(x,0,-1):
                    for c in range(4):
                        board[r][c] = board[r-1][c]     
                    
    # 특별한 칸 체크 (점수없음)
    cnt = 0
    for x in range(4,6):
        for y in range(4):
            if board[x][y]:
                cnt += 1
                break
    for _ in range(cnt):
        for r in range(9,0,-1):
            for c in range(4):
                board[r][c] = board[r-1][c]
        
# 빨간색 칸의 경계를 넘어가는 경우는 입력으로 주어지지 않는다.
for turn in range(N):
    t,x,y = map(int,input().split())
    if t==1:
        drop([[x,y]],board1)
        drop([[y,3-x]],board2) ## board2는 시계방향으로 회전한 상태로 구현
    elif t==2: #1X2
        drop([[x,y],[x,y+1]],board1)
        drop([[y,3-x],[y+1,3-x]],board2)
    elif t==3: #2X1
        drop([[x,y],[x+1,y]],board1)
        drop([[y,3-x],[y,2-x]],board2) 

print(score)
tiles = 0
for i in range(10):
    for j in range(4):
        if board1[i][j]: tiles += 1 
        if board2[i][j]: tiles += 1 
print(tiles)