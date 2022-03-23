from collections import deque

def solution(game_board, table):
    l1 = len(game_board)
    l2 = len(table)
    dx = [0,0,1,-1] # 동서남북
    dy = [1,-1,0,0]
    
    # 한 블록의 모든 (x,y)에 대하여 0이상 값을 갖도록 보정
    def revise(pos):
        MIN_x, MIN_y = min(p[0] for p in pos), min(p[1] for p in pos)
        newpos = [ (p[0]-MIN_x,p[1]-MIN_y) for p in pos]
        return newpos
    
    def bfs(i,j,graph,L,N):
        
        q = deque()
        q.append((i,j))
        graph[i][j]=-1 # 방문했다는 표시
        pos = [ (0,0) ] # 블럭의 위치를 저장하는 배열(처음 (i,j)를 (0,0)으로 세팅)
        
        while q:
            x,y = q.popleft()
            for dir in range(4):
                nx,ny = x+dx[dir],y+dy[dir]
                
                if nx>=L or nx<0 or ny>=L or ny<0: continue
                if graph[nx][ny]==-1: continue # 이미 방문한 칸이면
                if graph[nx][ny]!=N: continue # 탐색할 칸이 아니면
                q.append( (nx,ny) )
                graph[nx][ny]=-1
                pos.append( (nx-i,ny-j) ) # 처음 (i,j)에 대한 상대적인 위치
  
        return pos
    
    def find(_blank):
        for dir in range(4):
            for k in range(len(blocks)):
                block = rotated_blocks[dir][k]
                if used[k]: continue # k번째 블록 이미 썼으면 넘어가기
                if len(_blank)!=len(block): continue # 길이 다르면 넘어가기
                # block 같으면
                if set(_blank)==set(block):
                    used[k]=True
                    return len(_blank)
        # 맞는 block 없으면 0 리턴
        return 0
    
    
    
    # table에서 block찾기
    blocks = []
    for i in range(l2):
        for j in range(l2):
            if table[i][j]==1:
                blocks.append( revise( bfs(i,j,table,l2,1) ) ) 
     
    # game_board에서 blank찾기
    blanks = []
    for i in range(l1):
        for j in range(l1):
            if game_board[i][j]==0:
                blanks.append( revise( bfs(i,j,game_board,l1,0) ) ) 
                
    # blocks를 90도씩 회전한 좌표값 저장할 rotated_blocks(3차원) 생성         
    rotated_blocks =  [ blocks[:] ] # deepcopy # [ [blocks], [blocks 90도회전], ... ] (3차원배열)
  
    for rot in range(4):
        rotated_blocks.append( [ revise([(b[1],-b[0]) for b in block]) for block in rotated_blocks[rot]] )
    
    # game_board의 각각의 blank에 대하여 맞는  block 찾기     
    answer = 0       
    used = [False]*len(blocks) # 각각의 block이 사용되었는지 # 블록 썼으면 True, 아직 안썼으면 False
    for blank in blanks:
        answer += find(blank)
        
    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])) # 14