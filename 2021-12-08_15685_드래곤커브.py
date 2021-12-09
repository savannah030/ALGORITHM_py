# 문제를 잘읽자(x,y좌표반대)
# 3차원 배열 쓸 필요없음(정사각형의 기준을 "꼭지점"으로 보기 때문에 방향 저장할 필요없음)
# 방향배열을 일단 다 만들고 좌표찾기는 나중에! (좌표를 배열에 저장하는 건 의미없음)
import sys
input = sys.stdin.readline

N = int(input()) # 드래곤 커브의 개수 N(1 ≤ N ≤ 20)
board = [[False]*101 for _ in range(101)] # 동북서남 

dx = [1,0,-1,0] # 동북서남 
dy = [0,-1,0,1] 

for _ in range(N):
    x,y,d,g = map(int,input().split())
    board[x][y]=True
    dirs = []
    dirs.append(d)
    for _ in range(g):
        tmp = []
        for dir in dirs[::-1]: # 역순으로 탐색해야함
            tmp.append((dir+1)%4)
        dirs = dirs+tmp
    
    for dir in dirs:
        nx = x+dx[dir]
        ny = y+dy[dir]
        board[nx][ny]=True
        x,y = nx,ny # 좌표갱신 잊으면 안돼!
'''    
for i in range(101):
    print(board[i])
'''               
ans = 0   
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            ans += 1
print(ans)

