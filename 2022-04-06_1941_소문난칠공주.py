import sys
input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(input().rstrip()))
    
answer = dict()

dx = [0,0,1,-1] # 동서남북
dy = [1,-1,0,0]

def back(people):
    
    global answer,check
    
    # 임도연파가 4명 이상이면 가지치기
    if ''.join([board[p//5][p%5] for p in people]).count('Y')>3: return
    
    # 7명이 되면 answer에 중복된 people이 있는지 확인
    if len(people)==7:
        people = ''.join(map(str,sorted(people)))
        if people not in answer:
            answer[people] = 1
        return
      
    # 그룹의 모든 사람에 대하여 백트래킹 해야함
    # 케이스2 같이 분기되는 경우도 다 고려해야하기 때문
    for person in people:
        x,y = person//5,person%5
        # print("x=",x,"y=",y)
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if nx<0 or nx>=5 or ny<0 or ny>=5: continue
            # check[nxtperson]==True면 이미 만들어진 그룹
            nxtperson = nx*5+ny
            if check[nxtperson]: continue
            if nxtperson not in people:
                people.append(nxtperson)
                back(people[:])
                people.pop() 

# 해당 번호의 사람이 속하는 칠공주 그룹 구했는지 체크용           
check = [False]*25               
for person in range(25):
    x,y = person//5,person%5
    # 이다솜파 한명이 속하는 칠공주 그룹 모두 구하기
    if board[x][y]=='S':
        check[person]=True
        back([person])
    
print(len(answer.keys()))