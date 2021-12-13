import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split()) #세로,가로 4 ≤ N, M ≤ 500
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
        
def find(x,y): # ㅗ 모양은 동서남북 중 3개 고르는 combinations 이용
    global ans
    dir = [(0,-1),(0,1),(1,0),(-1,0)]
    for ndir in combinations(dir,3): # ndir = (0,-1),(0,1),(1,0)
        sum = board[x][y]
        for i in range(3):
            nx = x+ndir[i][0]
            ny = y+ndir[i][1]
            if nx<0 or nx>=N or ny<0 or ny>=M: break
            if ans >= sum+max_val*(3-i): break ## 가지치기
            sum += board[nx][ny]
        else: # for문 다 돌아야 ㅗ모양 만들어짐
            ans = max(ans,sum)

def find2(x,y,cnt,sum): # 나머지 모양은 dfs로 찾을 수 있음
    global ans,visited
    if ans >= sum+max_val*(4-cnt): # 가지치기
        return
    if cnt==4:
        ans = max(ans,sum)
        return ########
    for (nx,ny) in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if nx<0 or nx>=N or ny<0 or ny>=M: continue
        if visited[nx][ny]: continue
        visited[nx][ny]=True
        find2(nx,ny,cnt+1,sum+board[nx][ny])
        visited[nx][ny]=False

ans = 0            
visited = [ [False]*M for _ in range(N) ] 
max_val = max(map(max,board))
for i in range(N):
    for j in range(M):
        find(i,j)                # ㅗ모양
        visited[i][j]=True ########
        find2(i,j,1,board[i][j]) # 나머지 모양
        visited[i][j]=False ########

print(ans)