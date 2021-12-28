# 이분매칭: A 집단이 B 집단을 선택하는 방법에 대한 알고리즘
# 이분매칭 bfs로도 풀수있음!
# 주어진 정점들을 두 그룹으로 나누는 거기 때문에 9576 책나눠주기랑 다름!
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200005)

def bipartite(now,flag):
    group[now]=flag
    for nxt in graph[now]:
        if not group[nxt]:
            if not bipartite(nxt,-flag):
                return False
        elif group[nxt]==flag:
            return False
    return True

for K in range(int(input())):
    V,E = map(int,input().split()) # 정점,간선
    graph = [[] for _ in range(V)] # 정점 0번부터 시작
    for _ in range(E): 
        a,b = map(int,input().split())
        graph[a-1].append(b-1) # 정점 0번부터 시작하도록 바꾸기
        graph[b-1].append(a-1)
        
    group = [0]*V 
    for v in range(V): # 모든 점이 연결되어있지 않을 수도 있기 때문에 시작점만 dfs돌면 안됨(다 확인해줘야함)
        if not group[v]: # 그룹이 아직 정해지지 않았으면
            if not bipartite(v,1):
                print("NO")
                break
    else:
        print("YES")
    
        

    
    
        
        
        