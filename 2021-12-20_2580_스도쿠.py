import sys
input = sys.stdin.readline
# 1. row[r][n]=True <=> r번째 열에 n이 있다. 
# 2. sq 연산: (x//3)*3+y//3
# 3. 백트래킹 흐름 파악하기

def dfs1(n): 
    if n==len(zeros):
        for r in range(9):
            print(' '.join(map(str,board[r])))
        return True
    
    x,y = zeros[n]
    for num in range(1,10):
        if not row[x][num] and not col[y][num] and not sq[(x//3)*3+y//3][num]: 
            row[x][num] = col[y][num] = sq[(x//3)*3+y//3][num] = True
            board[x][y] = num
            if dfs1(n+1):    # dfs(n+1)이면 dfs(n+2),dfs(n+3),.. 계속 실행
                return True  # dfs(n+1)에서 만족하는 num이 없으면 밑에 백트래킹 실행
            row[x][num] = col[y][num] = sq[(x//3)*3+y//3][num] = False
            board[x][y] = 0
    return False 


def dfs2(n):
    if n==len(zeros):
        for r in range(9):
            print(' '.join(map(str,board[r])))
        sys.exit(0)
    
    x,y = zeros[n]
    for num in range(1,10):
        if not row[x][num] and not col[y][num] and not sq[(x//3)*3+y//3][num]: 
            row[x][num] = col[y][num] = sq[(x//3)*3+y//3][num] = True
            board[x][y] = num
            dfs2(n+1)
            row[x][num] = col[y][num] = sq[(x//3)*3+y//3][num] = False
            board[x][y] = 0

board = []
zeros = []
# 3차원 배열 쓸 필요없음
row = [ [False]*10 for _ in range(9)] #row[r][n]=True <=> r번째 열에 n이 있다. 
col = [ [False]*10 for _ in range(9)] 
sq = [ [False]*10 for _ in range(9)] 

for r in range(9):
    board.append(list(map(int,input().split())))
    for c in range(9):
        if board[r][c]==0:
            zeros.append((r,c))
        else:
            row[r][board[r][c]]=True
            col[c][board[r][c]]=True
            sq[((r//3)*3+c//3)][board[r][c]]=True
            
dfs1(0)

    


                 