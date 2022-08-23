# 모든 칸을 방문하기 위해 필요한 사다리 설치 비용의 최솟값
# 제일 큰 height 빼는 게 정답이 아님 !! (모두 이어진 상태가 아닐 수 있음)
# 1. 2146 다리만들기처럼 인덱싱
# 2. 인덱스 덩어리 w1,w2를 이어주는 간선 정보를 graph에 저장
# 3. 크루스칼 알고리즘으로 MST 만들기
# 47분+20분(디버깅)+11분(MST)
from collections import deque
def solution(land, height):
    N = len(land)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # 1
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
    
    # 2
    def setLadder(MAX_INDEX,indices):
        graph = []
       
        for x in range(N):
            for y in range(N):
                for dir in range(4):
                    nx,ny = x+dx[dir],y+dy[dir]
                    if nx<0 or nx>=N or ny<0 or ny>=N: continue
                    if indices[nx][ny]==indices[x][y]: continue
                    graph.append((abs(land[nx][ny]-land[x][y]),indices[x][y],indices[nx][ny]))
                    
        return graph
            
    MAX_INDEX,indices = indexing()
    graph = setLadder(MAX_INDEX,indices)
    # 3. 크루스칼 알고리즘
    # 3-1. 간선정보 비용에 따라 오름차순 정렬
    graph = sorted(graph,key=lambda x:x[0])
    parent = [x for x in range(MAX_INDEX+1)]
    
    def union_parent(x,y):
        px = find_parent(x)
        py = find_parent(y)
        
        if px<py:
            parent[py]=px
        else:
            parent[px]=py
    
    def find_parent(x):
        if parent[x]!=x:
            parent[x]=find_parent(parent[x])
        return parent[x]
    
    answer = 0
    # 모든 간선에 대해 사이클 판별해야함(중간에 break x)
    for (w,v1,v2) in graph:
        if find_parent(v1)!=find_parent(v2): # 3-2. 사이클이 발생하지 않으면
            union_parent(v1,v2)              # 3-3. 최소 신장 트리에 포함
            answer += w
    return answer


# 프림 알고리즘..??
import heapq
def solution_other(land, height):
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    N = len(land)
    visited = [ [False]*N for _ in range(N)]
    
    h=[(0,0,0)]
    answer = 0
    while h:
        cnt,x,y = heapq.heappop(h) 
        # visited 코드 순서가 평소 내가 쓰던 방식이랑 달라서 헷갈림 ㅠ
        if visited[x][y]: continue
        answer += cnt      
        visited[x][y] = True
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            if not visited[nx][ny]:
                temp = abs(land[x][y]-land[nx][ny])
                # height보다 차이가 크다면 그 차이를 넣어줘야함(사다리 건설비용)
                # height보다 작다면 사다리 건설비용이 들지 않기 때문에 0을 삽입
                if temp>height:
                    heapq.heappush(h,(temp,nx,ny))
                else:
                    heapq.heappush(h,(0,nx,ny))
    return answer

solution_other([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)
    
    