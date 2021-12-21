# 1시간 23분 pypy3 제출
import sys
input = sys.stdin.readline

board = []
for _ in range(10):
    board.append(list(map(int,input().split())))

paper = [5]*5
    
def check(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if i<0 or i>=10 or j<0 or j>=10: return False # 경계 밖으로 나가도 안되고
            if board[i][j]==2 or board[i][j]==0: return False # 겹쳐도 안 되고 0이 적힌 칸에는 색종이가 있으면 안 된다.
    return True
        
def dfs(x,y):
    
    global ans
    for n in range(5): 
        if paper[n]<0:  # 같은 종류 색종이 5장 이상 썼으면
            return      # return 하면 line 49에서 paper[n] 회복됨
        
    if (25-sum(paper))>ans: # 가지치기(ans보다 색종이를 많이 썼으면 가망없는 거니까)
        return
    
    for n in range(100):
        i,j = n//10,n%10
        if board[i][j]==1: # 아직 덮어야할 칸이 남아있으면 line 38로 감
            break
    else: # break문 안만났으면(더이상 덮어야할 칸이 없으면)
        tmp = 25-sum(paper)
        if 0<tmp<ans: # 답 갱신하고 return
            ans = tmp
            return
    
    for i in range(x,10):
        for j in range(10):
            if board[i][j]==1:
                for num in range(5,0,-1): 
                    if check(i,j,num):
                        
                        paper[num-1] -= 1
                        for x in range(i,i+num):
                            for y in range(j,j+num):
                                board[x][y]=2
                        dfs(i,j)                        #### 재귀
                        paper[num-1] += 1
                        for x in range(i,i+num):
                            for y in range(j,j+num):
                                board[x][y]=1
                                
                return ############ 한번의 dfs 턴에서는 하나의 점(i,j)만 확인하는 거기 때문에 return 꼭 붙여야함!!

ans = 25
if sum(map(sum,[board[i] for i in range(10)]))==0: # 처음부터 1이 적힌 칸이 없으면 필요한 색종이 수는 0개
    print(0)
else:
    dfs(0,0)
    if ans==25:
        print(-1)
    else:
        print(ans)