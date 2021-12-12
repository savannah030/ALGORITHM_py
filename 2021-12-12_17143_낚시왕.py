# 1시간 3분 
# board에 갱신하지 말고 sharks 배열에 저장했다가 한꺼번에 확인하는 게 좋을듯
import sys
input = sys.stdin.readline

# 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 
# 방향을 반대로 바꿔서 속력을 유지한채로 이동한다

# 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 
# 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.

dx = [-1,1,0,0] # 북남동서
dy = [0,0,1,-1]

R,C,M = map(int,input().split()) # 2 ≤ R, C ≤ 100, 0 ≤ 상어 수 M ≤ R×C
board = [[[] for _ in range(C)] for _ in range(R)]

sharks = []
for _ in range(M): #상어정보
    r, c, s, d, z = map(int,input().split()) #위치, 속력, 이동방향, 크기
    #(1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000)
    board[r-1][c-1].append((s,d-1,z)) #(속력,방향,크기)
    sharks.append((r-1,c-1,s,d-1,z))
'''
print("board initial")
for r in range(R):
    print(board[r])
'''
ans = 0
for king in range(C):
    for r in range(R):
        if len(board[r][king])==1: # 2.
            s,d,z = board[r][king].pop()
            sharks.remove((r,king,s,d,z))
            ans += z
            break
    
    # 3.move
    newsharks = []
    for shark in sharks:
        r,c,s,d,z = shark  
        remain = s
        nr = r+dx[d]*s
        nc = c+dy[d]*s
        while nr<0 or nr>=R:
            if nr<0: # 북으로 벗어남
                remain -= r
                r = 0
                d += 1 #북->남
            elif nr>=R: # 남
                remain -= (R-1-r)
                r = R-1
                d -= 1 #남->북
            nr = r+dx[d]*remain 
        while nc<0 or nc>=C:
            if nc<0: # 서
                remain -= c
                c = 0
                d -= 1 #서->동
            elif nc>=C: # 동
                remain -=(C-1-c)
                c = C-1
                d += 1
            nc = c+dy[d]*remain
        newsharks.append((nr,nc,s,d,z))
    
    board = [[[] for _ in range(C)] for _ in range(R)] #######
    newsharks = sorted(newsharks, key = lambda x: -x[4]) #크기가 큰 순으로 정렬
    alivesharks = []
    for newshark in newsharks:
        nr,nc,s,d,z = newshark
        if len(board[nr][nc])==0:
            board[nr][nc].append((s,d,z))
            alivesharks.append((nr,nc,s,d,z))
            
    sharks = alivesharks
    '''
    print("board king",king)
    for r in range(R):
        print(board[r])
    '''

print(ans)

        
    
        
    