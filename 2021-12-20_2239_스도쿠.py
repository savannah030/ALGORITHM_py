import sys
input = sys.stdin.readline

def check(r,c,num):
    for y in range(9):
        if board[r][y]==num:
            return False
        
    for x in range(9):
        if board[x][c]==num:
            return False
    
    startX = (r//3)*3 ###############
    startY = (c//3)*3
    for x in range(3):
        for y in range(3):
            if board[startX+x][startY+y]==num:
                return False
            
    return True


def dfs(n):
    if n==len(pos):
        for r in range(9):
            print("".join(map(str,board[r])))
        sys.exit(0)
        
    r,c = pos[n]
    for num in range(1,10):
        if check(r,c,num):
            board[r][c] = num
            dfs(n+1)
            board[r][c] = 0

board = []
for _ in range(9):
    board.append(list(map(int,input().rstrip())))
    
pos = []
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            pos.append((i,j))   
                            
dfs(0)

    

