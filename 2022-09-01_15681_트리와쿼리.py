import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# 48분
# 문제 잘 읽기 !! 
# 'R'을 루트로 갖는 트리 만들고 각각의 쿼리에 대한 서브쿼리 수 출력 !!

def makeChildrenTable(node):
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt]=True
            children[node].append(nxt)
            makeChildrenTable(nxt)

def makeAnswerTable(parent):
    tmp = children[parent]
    if not tmp:
        return 0
    
    for child in tmp:
        answer[parent] += (makeAnswerTable(child)+1)
        
    return answer[parent]

N,R,Q = map(int,input().split()) #정점의수,루트번호,쿼리수
graph = [ [] for _ in range(N+1)]
for _ in range(N-1):
    U,V = map(int,input().split())
    graph[U].append(V)
    graph[V].append(U)

children = [ [] for _ in range(N+1) ]
answer = [0]*(N+1)
visited = [False]*(N+1)

visited[R] = True
makeChildrenTable(R)

answer = [0]*(N+1)
makeAnswerTable(R)

for _ in range(Q):
    print(answer[int(input())]+1) # 자기자신까지 포함

    
    
    