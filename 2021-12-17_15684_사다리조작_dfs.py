# deepcopy 쓸 필요없음
# 사다리 1개 2개 3개 순차적으로 검색하면 그렇지 않지만 
# 한번에 재귀로 할 때 3개짜리로 답을 찾은 후에 1개짜리 답이 나왔을 때 재설정하는 로직을 안짜주면 12프로에서 틀립니다. 
import sys
input = sys.stdin.readline

N,M,H = map(int,input().split()) #세로선개수,가로선개수,세로선마다 가로선을 놓을 수 있는 위치

board = [ [False]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int,input().split())  #b~b+1 세로선을 a번 점선 위치에서 연결
    # 0번부터 시작하도록 바꾸기
    board[a-1][b-1]=True
    
def check(_board): 
      
    for n in range(N):
        now = n
        for h in range(H):
            if now<N-1 and _board[h][now]:
                now += 1
            elif now>0 and _board[h][now-1]:
                now -= 1
        if now!=n: 
            return False
    return True 
    
def dfs(h,cnt): # 사다리 재귀적으로 설치
    global ans,board
    if cnt>=4:
        return

    if check(board):
        if ans==-1: ans=cnt
        else: ans = min(ans,cnt)
        return 
    
    for x in range(h,H):
        for y in range(N-1): # 마지막 세로선은 확인할 필요없음
            if not board[x][y]:
                if y==0 and not board[x][y+1] or 0<y<N-1 and not board[x][y-1] and not board[x][y+1]:
                    board[x][y]=True
                    dfs(x,cnt+1) 
                    board[x][y]=False

ans = -1          
dfs(0,0)
print(ans)
