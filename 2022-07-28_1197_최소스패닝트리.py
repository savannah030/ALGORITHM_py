import sys
input = sys.stdin.readline
## 크루스칼 알고리즘
# 1. 간선 정보를 오름차순으로 정렬 (인접행렬x,인접그래프x)
# 2. 매 간선마다 사이클이 발생하는지 확인

def union_parent(x,y):
    px = find_parent(x)
    py = find_parent(y)
    
    if px<py:
        parent[py] = px
    else:
        parent[px] = py

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]
            
V,E = map(int,input().split())
answer = 0
graph = [] 
parent = [i for i in range(V+1)] # 1번부터 시작
for _ in range(E):
    graph.append(tuple(map(int,input().split()))) #(A,B,C)
graph = sorted(graph, key=lambda x: x[2]) 

for (A,B,C) in graph:
    if find_parent(A)==find_parent(B):
        continue
    else:
        answer += C
        union_parent(A,B)
print(answer)
   
    