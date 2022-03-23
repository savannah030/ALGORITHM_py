from collections import deque

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
    for i in range(l2):
        for j in range(l2):
            if table[i][j]:
                rotated_blocks[0].append(bfs(i,j)) # 18분
    
    used = [False]*len(rotated_blocks[0]) # 블록 썼으면 True, 아직 안썼으면 False

    # 시계방향으로 90도 회전
    for r in range(3):
        for block in rotated_blocks[r]:
            newblock = []
            for (x,y) in block:
                newblock.append((y,-x)) # 32분
            rotated_blocks[r+1].append(newblock)
        
    '''
    for i in range(len(rotated_blocks)): # 42분
        print(i, rotated_blocks[i])
    0 [[(0, 0), (1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (1, 0), (1, -1), (2, 0)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (0, 1)]]
    1 [[(0, 0), (0, -1)], [(0, 0), (1, 0), (1, -1), (1, -2), (2, -2)], [(0, 0), (0, -1), (-1, -1), (0, -2)], [(0, 0), (1, 0), (1, -1)], [(0, 0), (1, 0)]]
    2 [[(0, 0), (-1, 0)], [(0, 0), (0, -1), (-1, -1), (-2, -1), (-2, -2)], [(0, 0), (-1, 0), (-1, 1), (-2, 0)], [(0, 0), (0, -1), (-1, -1)], [(0, 0), (0, -1)]]
    3 [[(0, 0), (0, 1)], [(0, 0), (-1, 0), (-1, 1), (-1, 2), (-2, 2)], [(0, 0), (0, 1), (1, 1), (0, 2)], [(0, 0), (-1, 0), (-1, 1)], [(0, 0), (-1, 0)]]
    '''
        
    
    #new_game_board = [ [0 if game_board[x][y] else 1 for y in range(l1)] for x in range(l2)] # 53분 삽질 그냥 새로 함수 만드는게 나음..
    #print("new",new_game_board)
    
       
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
    
    blanks = []
    for x in range(l1):
        for y in range(l1):
            if not game_board[x][y]: #빈칸이면
                blanks.append(findBlanks(x,y))
    # print("blanks",blanks)
    # blanks [[(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (1, 0)], [(0, 0), (0, 1), (1, 0)], [(0, 0), (1, 0), (1, 1), (1, -1)], [(0, 0), (1, 0), (1, -1)], [(0, 0)]]
    '''
    0 2 [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    0 5 [(0, 0), (1, 0)]
    1 0 [(0, 0), (0, 1), (1, 0)]
    3 2 [(0, 0), (1, 0), (1, 1), (1, -1)]
    4 5 [(0, 0), (1, 0), (1, -1)]
    5 0 [(0, 0)]
    '''
    answer = 0 # 총 몇칸을 채울 수 있는지
    for blank in blanks:
        print("blank",blank)
        for i in range(4):
            for j in range(len(rotated_blocks[i])): #for block in rotated_blocks[r]:
                block = rotated_blocks[i][j]
                #if game_board[blank[0][0]][blank[0][1]]: continue # 이미 채워져있으면 근데 코드 좀..... ##############
                if used[j]: continue
                if len(blank)!=len(block): continue
                if set(blank)==set(block): ###### 탐색 순서가 다른 경우 좌표가 맞지 않음................ # 1시간 23분
                    ################## 왜 처음엔 생각 못했을까...........
                    answer += len(blank)
                    print(block,blank)
                    for (x,y) in blank:
                        game_board[blank[0][0]+x][blank[0][1]+y]=True
                    used[j]=True

    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])) # 14