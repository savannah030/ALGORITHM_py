# 이분매칭: A 집단이 B 집단을 선택하는 방법에 대한 알고리즘
# 이분매칭 bfs로도 풀수있음!
# 주어진 정점들을 두 그룹으로 나누는 거기 때문에(두 그룹 왔다갔다해야함) 9576 책나눠주기(그리디)랑 다름!
### 이분그래프!=이분매칭 같은 개념 아님!!!! https://www.crocus.co.kr/499
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200005)

def bipartite(now,flag):
    group[now]=flag
    for nxt in graph[now]:
        if not group[nxt]: # 아직 그룹이 정해지지 않은 nxt에 한해서만 확인
            if not bipartite(nxt,-flag): # nxt로 bipartite함수 재귀호출. nxt부터가 이분그래프가 아니면
                return False             # 이번 now부터의 그래프도 이분그래프가 아닌것이 당연
        elif group[nxt]==flag: # group[nxt]!=0이어서 이미 방문한 노드는 맞는데, now랑 그룹이 같으면 
            return False       # 이분그래프가 아님
    return True # 모든 nxt가 이분그래프이면 now도 이분그래프가 맞음

for K in range(int(input())):
    V,E = map(int,input().split()) # 정점,간선
    graph = [[] for _ in range(V)] # 정점 0번부터 시작
    for _ in range(E): 
        a,b = map(int,input().split())
        graph[a-1].append(b-1) # 정점 0번부터 시작하도록 바꾸기
        graph[b-1].append(a-1)
        
    group = [0]*V # 0으로 초기화. bipartite함수에서 정점 지날때마다 1,-1,1,-1,.. 번갈아가며 값 할당(이분그래프 특징)
    for v in range(V): # 모든 점이 연결되어있지 않을 수도 있기 때문에 시작점만 dfs돌면 안됨(다 확인해줘야함)
        if not group[v]: # 그룹이 아직 정해지지 않았을때만 bipartite 함수실행
            if not bipartite(v,1): 
                print("NO")
                break
    else:
        print("YES")
    
        

    
    
        
        
        