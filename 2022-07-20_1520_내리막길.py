# 1937 욕심쟁이 판다(dfs+dp)와 비슷
# 20분,,, 흠,, 비슷한데 왜 생각 못하지
# 28분,,, 탐색 순서는 알겠는데,,, 알고리즘을 못짜겠다
# 1시간 12분
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

M,N = map(int,input().split()) # 세로,가로
board = []
dp = [ [-1]*N for _ in range(M) ]
for _ in range(M):
    board.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if x==M-1 and y==N-1:
        return 1
    # 메모이제이션
    if dp[x][y]>=0:
        return dp[x][y]
    dp[x][y]=0 # 방문표시
    for dir in range(4):
        nx,ny = x+dx[dir],y+dy[dir]
        if nx<0 or nx>=M or ny<0 or ny>=N: continue
        # 도착점에 도착한 후엔 4방향에 작은 거 나올때까지 되돌아감
        if board[nx][ny]<board[x][y]:
            dp[x][y] += dfs(nx,ny) ########
    return dp[x][y]

print(dfs(0,0))