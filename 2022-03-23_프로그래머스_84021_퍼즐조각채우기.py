from collections import deque

## (x,y)의 x,y가 모두 0 이상이도록 보정해야함
## 반복되는 코드 함수로 만들어서 줄이기

def solution(game_board, table):
    l1 = len(game_board)
    l2 = len(table)
    dx = [0,0,1,-1] # 동,서,남,북
    dy = [1,-1,0,0]
    
    def bfs(i,j): # bfs
        pos = [ (0,0) ] # 블럭의 위치를 저장하는 배열(처음 (i,j)를 (0,0)으로 세팅)
        q = deque()
        table[i][j]=0 # 이미 방문했다는 표시
        q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for dir in range(4):
                nx,ny = x+dx[dir],y+dy[dir]
                # 범위 벗어나면 다음칸 탐색
                if nx>=l2 or nx<0 or ny>=l2 or ny<0: continue
                # 블럭이 아니면 다음칸 탐색
                if not table[nx][ny]: continue 
                # 블럭이면
                table[nx][ny]=0 # 이미 방문했다는 표시
                pos.append((nx-i,ny-j)) # 처음 (i,j)에 대한 상대적인 위치
                q.append((nx,ny))
                
        return pos
    
    # table에 놓인 블럭의 좌표들을 저장하는 배열
    # blocks[0]=원본, blocks[1]=90도회전, blocks[2]=180도회전, blocks[3]=270도회전
    rotated_blocks = [ [] for _ in range(4)] 

    tempblocks = []
    for i in range(l2):
        for j in range(l2):
            if table[i][j]:
                tempblocks.append(bfs(i,j)) 
    for tempblock in tempblocks:
        MIN_x, MIN_y = min(tb[0] for tb in tempblock),min(tb[1] for tb in tempblock)
        newblock = [ (tb[0]-MIN_x,tb[1]-MIN_y) for tb in tempblock ]
        rotated_blocks[0].append(newblock)

    
    used = [False]*len(rotated_blocks[0]) # 블록 썼으면 True, 아직 안썼으면 False

    # 시계방향으로 90도 회전
    for r in range(3):
        for block in rotated_blocks[r]:
            tempblock = []
            newblock = []
            for (x,y) in block:
                tempblock.append((y,-x)) 
            ##### TODO: newblock의 (x,y)가 모두 양수이도록 고치기
            MIN_x, MIN_y = min(tb[0] for tb in tempblock),min(tb[1] for tb in tempblock)
            newblock = [ (tb[0]-MIN_x,tb[1]-MIN_y) for tb in tempblock ]
            rotated_blocks[r+1].append(newblock)
    '''
    for i in range(len(rotated_blocks)): 
        print(i, rotated_blocks[i])
    0 [[(0, 0), (1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 1), (1, 1), (1, 0), (2, 1)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (0, 1)]]
    1 [[(0, 1), (0, 0)], [(0, 2), (1, 2), (1, 1), (1, 0), (2, 0)], [(1, 2), (1, 1), (0, 1), (1, 0)], [(0, 1), (1, 1), (1, 0)], [(0, 0), (1, 0)]]
    2 [[(1, 0), (0, 0)], [(2, 2), (2, 1), (1, 1), (0, 1), (0, 0)], [(2, 0), (1, 0), (1, 1), (0, 0)], [(1, 1), (1, 0), (0, 0)], [(0, 1), (0, 0)]]
    3 [[(0, 0), (0, 1)], [(2, 0), (1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (1, 1), (0, 2)], [(1, 0), (0, 0), (0, 1)], [(1, 0), (0, 0)]]
    '''
       
    def findBlanks(i,j): # bfs
        pos = [ (0,0) ] # 블럭의 위치를 저장하는 배열(처음 (i,j)를 (0,0)으로 세팅)
        q = deque()
        game_board[i][j]=1 # 이미 방문했다는 표시
        q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for dir in range(4):
                nx,ny = x+dx[dir],y+dy[dir]
                # 범위 벗어나면 다음칸 탐색
                if nx>=l2 or nx<0 or ny>=l2 or ny<0: continue
                # 빈칸이 아니면 다음칸 탐색
                if game_board[nx][ny]: continue 
                # 빈칸이면
                game_board[nx][ny]=1 # 이미 방문했다는 표시
                pos.append((nx-i,ny-j)) # 처음 (i,j)에 대한 상대적인 위치
                q.append((nx,ny))
                
        return pos
    
    tempblanks = []
    newblanks = []
    for x in range(l1):
        for y in range(l1):
            if not game_board[x][y]: #빈칸이면
                tempblanks.append(findBlanks(x,y))
    for tempblank in tempblanks:
            MIN_x, MIN_y = min(tb[0] for tb in tempblank),min(tb[1] for tb in tempblank)
            newblank= [ (tb[0]-MIN_x,tb[1]-MIN_y) for tb in tempblank ]
            newblanks.append(newblank)
    print("newblanks=",newblanks)
    # [[(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (1, 0)], [(0, 0), (0, 1), (1, 0)], [(0, 0), (1, 0), (1, 1), (1, -1)], [(0, 0), (1, 0), (1, -1)], [(0, 0)]]
    # newblanks= [[(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (1, 0)], [(0, 0), (0, 1), (1, 0)], [(0, 1), (1, 1), (1, 2), (1, 0)], [(0, 1), (1, 1), (1, 0)], [(0, 0)]]
    def put(_blank):
        print("_blank",_blank)
        for dir in range(4):
            for k in range(len(rotated_blocks[dir])):
                block = rotated_blocks[dir][k]
            
                if used[k]: 
                    #print(2)
                    continue
                if len(_blank)!=len(block): 
                    #print(3)
                    continue
                if set(_blank)==set(block):
                    print(block,_blank)
                    for (x,y) in _blank:
                        game_board[_blank[0][0]+x][_blank[0][1]+y]=1
                    used[k]=True
                    return len(_blank)
        return 0
                   
              
    answer = 0 # 총 몇칸을 채울 수 있는지  
   
    for blank in newblanks:
        k = put(blank)
        print("k=",k)
        answer += k ## game_board의 각각의 빈칸에 대하여 table의 조각으로 채움
        
                    
   
    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])) # 14