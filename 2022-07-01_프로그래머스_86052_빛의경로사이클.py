# 48분
def solution(grid):
    R,C = len(grid),len(grid[0])
    # 무조건 나가는 방향으로만 생각
    visited = [[[False]*4 for y in range(C)] for x in range(R)]
    dx = [1,0,-1,0] #남동북서
    dy = [0,1,0,-1]

    answer = []

    # 모든 칸,방향에 대해 다 탐색해야함!
    for r in range(R):
        for c in range(C):
            for dir in range(4):

                nx,ny,cnt = r,c,0

                while True:
                    x,y = nx,ny
                    if visited[x][y][dir]: break

                    visited[x][y][dir]=True
                    cnt += 1

                    # 방향 바꾸기
                    if grid[x][y]=='L': dir = (dir+1)%4
                    elif grid[x][y]=='R': dir = (dir-1)%4

                    nx,ny = (x+dx[dir])%R,(y+dy[dir])%C ### 나머지 이용

                if cnt>0:
                    answer.append(cnt)   

    return sorted(answer)


# 무조건 나가는 방향으로만 생각하기(in/out 생각하지 말기)
def wrong(grid):
    #visited[x][y][dir][in/out]
    R,C = len(grid),len(grid[0])
    visited = [[[[False]*2 for dir in range(4)] for y in range(C)] for x in range(R)]
    dx = [1,0,-1,0] #남동북서
    dy = [0,1,0,-1]
    
    answer = []
 
    # (0,0)에서 4방향 다 탐색
    for dir in range(4):
        nx,ny,cnt = 0,0,0
        
        while True:
            
            x,y = nx,ny
    
            if visited[x][y][dir][1]:
                break
                
            visited[x][y][dir][1]=True
          
            # 방향 바꾸기
            if grid[x][y]=='L':
                dir = (dir+1)%4
            elif grid[x][y]=='R':
                dir = (dir-1)%4
                
            nx,ny = x+dx[dir],y+dy[dir]
                
            if nx<0 or nx>=R or ny<0 or ny>=C:
                if dir==0: # 남
                    nx = 0
                    visited[nx][ny][2][0]=True
                elif dir==1: # 동
                    ny = 0
                    visited[nx][ny][3][0]=True
                elif dir==2: # 북
                    nx = R-1
                    visited[nx][ny][0][0]=True
                elif dir==3: # 서
                    ny = C-1
                    visited[nx][ny][1][0]=True
            else:
                if visited[nx][ny][(dir-2)%4][0]:
                    break
            cnt += 1
            
        if cnt>0:
            answer.append(cnt)   
    
    return sorted(answer)