# 48분(1차시도) 경사로 놓는 조건 구현이 까다로움
# 23분 높이가 같으면 그냥 넘어가고 
# 내리막길이나 오르막길이 나왔을 때부터 for(L) 돌리면 됨
import sys
input = sys.stdin.readline

N,L = map(int,input().split())

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))  

def check(line):
    slope = [False]*N
    for i in range(1,N):
        # 내리막길
        if line[i]<line[i-1]: 
            # 높이가 1 이상이면 안됨
            if abs(line[i]-line[i-1])>1: return False
            for j in range(i,i+L):
                # 범위 벗어나면 안됨
                if j>N-1: return False
                # 경사로를 또 놓으면 안됨
                if slope[j]: return False
                slope[j]=True
                
        # 오르막길
        elif line[i]>line[i-1]: 
            # 높이가 1 이상이면 안됨
            if abs(line[i]-line[i-1])>1: return False
            for j in range(i-1,i-L-1,-1):
                # 범위 벗어나면 안됨
                if j<0: return False
                # 경사로를 또 놓으면 안됨
                if slope[j]: return False
                slope[j]=True
                
        else: continue #######line[i]==line[i-1]이면 그냥 넘어가는 게 제일 간단함 

    return True

ans = 0
for line in board:
    if check(line): ans += 1 
    
# rotate
newboard = [[0]*N for _ in range(N)] 
for i in range(N):
    for j in range(N):
        newboard[i][j] = board[j][N-1-i]
    
for line in newboard:
    if check(line): ans += 1  
print(ans)  
    