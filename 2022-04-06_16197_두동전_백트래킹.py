import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 1<=세로,가로<=20
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

coins = []
for i in range(N):
    for j in range(M):
        if board[i][j]=='o':
            coins.append((i,j))
        
dx = [0,0,1,-1]
dy = [1,-1,0,0]
    
def back(cnt,coins):
    global answer
    
    # 가지치기
    if cnt>answer or cnt>10:
        return
  
    for dir in range(4):
        dropped = 0
        newcoins = [] # 동전이 떨어지지 않을 경우만 좌표 추가
        for coin in coins:
            x,y = coin
            nx,ny = x+dx[dir],y+dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                dropped += 1
                continue
            # 벽이면 좌표 그대로
            if board[nx][ny]=='#':
                newcoins.append((x,y))
            # 벽이 아니면 한칸 이동
            else:
                newcoins.append((nx,ny))
              
        if dropped==2:
            continue # 다른 방향도 봐야하므로 continue
        if dropped==1:
            answer = min(answer,cnt)
            return # 답이 나왔으므로 더이상 볼 필요없음 따라서 continue가 아닌 return
        if dropped==0:
            back(cnt+1,newcoins)
    
answer = 11 
back(1,coins)
if answer==11:
    print(-1)
else:
    print(answer)