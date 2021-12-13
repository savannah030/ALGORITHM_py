import sys
input = sys.stdin.readline

N,M,x,y,K = map(int,input().split()) #세로,가로,처음좌표(x,y),명령수

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
'''
print("board")
for i in range(N):
    print(board[i])
'''  
dx = [0,0,-1,1] # 동서"""북남""" (문제를잘읽자)
dy = [1,-1,0,0]
dice = [11,0,0,0,0,0,0] # 10미만의 수 
cmds = list(map(int,input().split()))
#print("cmds=",cmds)
for cmd in cmds:
    nx = x+dx[cmd-1]
    ny = y+dy[cmd-1]
    if nx<0 or nx>=N or ny<0 or ny>=M: 
        continue # 명령 무시 but 윗면은 그대로 출력
    
    if cmd==1: #동
        dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
    elif cmd==2: #서
        dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
    elif cmd==3: #북
        dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]
    else: #elif cmd==4: #남
        dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5] 
    
    print(dice[1]) #print("cmd=",cmd,"dice[1]=",dice[1]) # 윗면 출력 
    
    if board[nx][ny]==0:  # 이동한 칸에 쓰여 있는 수가 0이면
        board[nx][ny]=dice[6] # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    else: # 0이 아닌 경우
        dice[6]=board[nx][ny] # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 
        board[nx][ny]=0 # 칸에 쓰여 있는 수는 0
    x,y = nx,ny 
   
    
        
    
    




