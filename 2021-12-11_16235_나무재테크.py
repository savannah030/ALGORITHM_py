# r과 c는 1부터 시작
# 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다. (문제 잘읽자)
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split()) #칸수,나무수,K년
board = [ [5]*N for _ in range(N)]
A = [] # 처음 양분의 양
for _ in range(N):
    A.append(list(map(int,input().split()))) 

trees = [ [ [] for _ in range(N)] for _ in range(N)]
dead = [ [ [] for _ in range(N)] for _ in range(N)]
    
for _ in range(M):
    x,y,z = map(int,input().split()) # 나무의위치(x,y), 나이 z
    trees[x-1][y-1].append(z) # 1번부터 시작
    # 입력으로 주어지는 나무의 위치는 모두 서로 다름(정렬할 필요없음)
'''
print("year=",0) 
print("board")
for r in range(N):
    print(board[r])
    
for r in range(N):
    for c in range(N):
        print(trees[r][c],end=' ')
    print('\n')
'''
for year in range(K):
    
    # 봄
    for r in range(N):
        for c in range(N):
            if len(trees[r][c])==0: continue
            trees[r][c].sort()
            # 나이가 어린 나무부터 양분을 먹는다.
            for i in range(len(trees[r][c])):
                tree = trees[r][c][i]
                if (board[r][c]-tree)<0: # 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는
                    # 양분을 먹지 못하고 즉시 죽는다.
                    dead[r][c].extend(trees[r][c][i:]) 
                    trees[r][c] = trees[r][c][:i] 
                    break
                board[r][c]-=tree # 자신의 나이만큼 양분을 먹고 양분 없어지는 거 아님!!!!!!! 제발 문제 멋대로 해석하지 말자
                trees[r][c][i] += 1 # 나이가 1 증가
    
    # 여름
    for r in range(N):
        for c in range(N):
            for i in range(len(dead[r][c])): ######### 한번에 더하면 다른 값 나오나?
                board[r][c] += (dead[r][c][i]//2)
            dead[r][c] = [] # 초기화

    # 가을
    for r in range(N):
        for c in range(N):
            for i in range(len(trees[r][c])):
                if (trees[r][c][i]%5)==0:
                    for (nr,nc) in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                        if nr<0 or nr>=N or nc<0 or nc>=N: continue
                        trees[nr][nc].append(1) ################### 어차피 정렬할거니까 

    # 겨울
    for r in range(N):
        for c in range(N):
            board[r][c] += A[r][c]
    '''  
    print("year=",year+1)     
    print("board")
    for r in range(N):
        print(board[r])
            
    print("trees")
    for r in range(N):
        for c in range(N):
            print(trees[r][c],end=' ')
            #print("r=",r,"c=",c,trees[r][c],end=' ')
        print('\n')
    ''' 
  
ans = 0     
for r in range(N):
    for c in range(N):
        ans += len(trees[r][c])
print(ans)

            
            
    
