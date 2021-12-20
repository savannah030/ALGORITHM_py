import sys
input = sys.stdin.readline

R,C = map(int,input().split())

# 1번부터 시작
board = []
for _ in range(R):
    board.append(list(input().rstrip()))
    
dx = [0,0,1,-1]
dy = [1,-1,0,0]
   
def dfs(x,y,cnt):
    global ans
    if cnt>ans: ans = cnt
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<R and 0<=ny<C and not alpha[ord(board[nx][ny])-65]: 
            alpha[ord(board[nx][ny])-ord('A')]=True
            dfs(nx,ny,cnt+1)
            alpha[ord(board[nx][ny])-ord('A')]=False


ans = 0
alpha = [False]*26
alpha[ord(board[0][0])-65]=True
dfs(0,0,1)
print(ans)