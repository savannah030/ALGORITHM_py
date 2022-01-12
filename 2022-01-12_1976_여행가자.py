import sys
input = sys.stdin.readline

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

N = int(input()) # 도시의수<=200
M = int(input()) # 여행 계획에 속한 도시들의 수<=1000
parent = [i for i in range(N)]
graph = [] # 단방향 그래프(0번부터시작)
for _ in range(N):
    graph.append(list(map(int,input().split())))    
    
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            union_parent(i,j)
    
plans = list(map(int,input().split())) # 1번부터 시작
p = parent[plans[0]-1]
for plan in plans[1:]:
    plan -= 1 # 0번부터 시작
    if parent[plan]!=p:
        print("NO")
        break
else:
    print("YES")
    
    

