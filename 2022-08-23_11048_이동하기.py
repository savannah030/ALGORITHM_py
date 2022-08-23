import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

# 시간 줄이기
# board[x][y]에서 최대로 먹을 수 있는 사탕값 dp[x+1][y+1]에 저장
dp = [ [0 for m in range(M+1)] for n in range(N+1) ]
for x in range(1,N+1):
    for y in range(1,M+1):
        dp[x][y] = board[x-1][y-1]+max(dp[x-1][y],dp[x][y-1],dp[x-1][y-1])
            
print(dp[N][M])

# 16분 메모리 70MB, 시간 3000ms 너무 비효율적이야,,,
'''
dx = [1,0,1] # 방향주의 !!
dy = [0,1,1]
dp = [ [board[n][m] for m in range(M)] for n in range(N) ]
for x in range(N):
    for y in range(M):
        for dir in range(3):
            nx,ny = x+dx[dir],y+dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=M: continue
            dp[nx][ny] = max(dp[nx][ny],dp[x][y]+board[nx][ny])
            
print(dp[N-1][M-1])
'''
            
