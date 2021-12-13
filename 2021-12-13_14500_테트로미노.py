# python은 시간초과 (visited배열넣다뺌,가지치기안함 때문에 그런듯)
import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split()) #세로,가로 4 ≤ N, M ≤ 500
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

cand = []
def dfs(x,y,visited,sum): 
    if len(visited)==4:
        cand.append(sum)
        return #################
    for (nx,ny) in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if nx<0 or nx>=N or ny<0 or ny>=M: continue
        if (nx,ny) in visited: continue
        visited.append((nx,ny))
        dfs(nx,ny,visited[:],sum+board[nx][ny])
        visited.pop()

        
def find(x,y): #ㅗ
    dir = [(0,-1),(0,1),(1,0),(-1,0)]
    for ndir in combinations(dir,3): # ndir = (0,-1),(0,1),(1,0)
        sum = board[x][y]
        for i in range(3):
            nx = x+ndir[i][0]
            ny = y+ndir[i][1]
            if nx<0 or nx>=N or ny<0 or ny>=M: break
            sum += board[nx][ny]
        else:
            cand.append(sum)

for i in range(N):
    for j in range(M):
        dfs(i,j,[(i,j)],board[i][j])
        find(i,j) #ㅗ

print(max(cand))