# 모든 칸을 방문하기 위해 필요한 사다리 설치 비용의 최솟값
# 2146 다리만들기처럼 인덱싱한다음 각 덩어리마다 height 가장 적은
# 47분+20분
# 시간초과는 그렇다 치는데 어디서 틀리는거지,,, 
from collections import deque
def solution(land, height):
    N = len(land)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def indexing():
        q = deque()
        indices = [ [-1]*N for _ in range(N)]
        INDEX = 0
        for i in range(N):
            for j in range(N):
                if indices[i][j]==-1:
                    indices[i][j]=INDEX
                    q.append((i,j))
                    while q:
                        x,y = q.popleft()
                        for dir in range(4):
                            nx,ny = x+dx[dir],y+dy[dir]
                            if nx<0 or nx>=N or ny<0 or ny>=N: continue
                            if indices[nx][ny]==-1 and abs(land[nx][ny]-land[x][y])<=height:
                                indices[nx][ny]=INDEX
                                q.append((nx,ny))
                    INDEX += 1
     
        return INDEX-1,indices
    
    # (최대 인덱스)-1 개 놓으면 됨
    def setLadder(MAX_INDEX,indices):
        ladders_matrix = [ [10001]*(MAX_INDEX+1) for _ in range(MAX_INDEX+1)]
       
        for x in range(N):
            for y in range(N):
                for dir in range(4):
                    nx,ny = x+dx[dir],y+dy[dir]
                    if nx<0 or nx>=N or ny<0 or ny>=N: continue
                    if indices[nx][ny]==indices[x][y]: continue
                    elif ladders_matrix[indices[x][y]][indices[nx][ny]]>abs(land[nx][ny]-land[x][y]):
                        ladders_matrix[indices[x][y]][indices[nx][ny]]=abs(land[nx][ny]-land[x][y])
                        ladders_matrix[indices[nx][ny]][indices[x][y]]=abs(land[nx][ny]-land[x][y])
    
        cands = []
        for st,info in enumerate(ladders_matrix[:-1]):
            cands.extend([i for i in info[st+1:] if i<10001])
                          
        return cands
            
    MAX_INDEX,indices = indexing()
    cands = setLadder(MAX_INDEX,indices)
    cands.sort()
    return sum(cands[:MAX_INDEX])
    