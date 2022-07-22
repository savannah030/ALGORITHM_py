import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
board = []
dp = [ [1]*n for _ in range(n) ]
for _ in range(n):
    board.append(list(map(int,input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    # dp값이 이미 있으면 그 칸만큼 더 이동할 수 있음
    if dp[x][y]>1:
        return dp[x][y]
    for dir in range(4):
        nx,ny = x+dx[dir],y+dy[dir]
        if nx<0 or nx>=n or ny<0 or ny>=n: continue
        # 도착점에 도착한 후엔 4방향에 작은 거 나올때까지 되돌아감
        if board[nx][ny]>board[x][y]:
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

answer = 1
for i in range(n):
    for j in range(n):
        answer = max(answer,dfs(i,j))
print(answer)