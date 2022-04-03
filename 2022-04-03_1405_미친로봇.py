import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))
N = arr[0]
prob = [0.01*a for a in arr[1:]]

dx = [0,0,1,-1] # 동서남북
dy = [1,-1,0,0]

def back(n,routes,x,y,tmp):
    global answer
    if n==0:
        answer += tmp
        return
    for dir in range(4):
        nx,ny = x+dx[dir],y+dy[dir]
        if (nx,ny) in routes: # 이동경로가 단순하지 않으면 가지치기
            continue
        # 이동경로가 단순하면
        routes.add((nx,ny))
        back(n-1,routes,nx,ny,tmp*prob[dir])
        routes.remove((nx,ny))
        
answer = 0
back(N,{(0,0)},0,0,1)
print(answer)
