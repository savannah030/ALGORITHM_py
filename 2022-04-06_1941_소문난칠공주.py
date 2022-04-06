import sys
input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(input().rstrip()))
    
answer = dict()

dx = [0,0,1,-1] # 동서남북
dy = [1,-1,0,0]

def back(people):
    
    global answer
    
    # 임도연파가 4명 이상이면 가지치기
    if ''.join([board[p//5][p%5] for p in people]).count('Y')>3: return
    
    # 7명이 되면 answer에 중복된 people이 있는지 확인
    if len(people)==7:
        people = ''.join(map(str,sorted(people)))
        if people not in answer:
            answer[people] = 1
        return
      
    for person in people:
        x,y = person//5,person%5
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if nx<0 or nx>=5 or ny<0 or ny>=5: continue
            
            adj = nx*5+ny
            if adj not in people:
                people.append(adj)
                back(people[:])
                people.pop() 
                
for person in range(25):
    back([person])
    
print(len(answer.keys()))