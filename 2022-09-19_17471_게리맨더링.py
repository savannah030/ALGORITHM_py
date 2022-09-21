# 57분
import sys
input = sys.stdin.readline
from collections import deque
INF = int(10e9)

# 모두 연결되었는지 확인법? -> flood fill
# 노드 추가하면 가능한 경우 있음 (예1->예3->예2)
# 그러니까 중간에 return 하면 안됨
# 그리고 지금까지 탐색한 게 앞으로의 결과와 아무 상관이 없기 때문에 combinations 쓰기(백트래킹 말고,,,)

N = int(input())
populations = list(map(int,input().split())) # 1번->populations[0]에 저장
graph = []  #1번->graph[0]에 저장
for _ in range(N):
    graph.append([item-1 for item in list(map(int,input().split()))[1:]])
    
ans = INF
vis = [False]* (1<<N)

# flood fill
def bfs(group):
    
    print("start=",bin(group))
    q = deque()
    # 노드 1개 추가
    for node in range(N):
        if group&(1<<node):
            q.append(node)
            group &= ~(1<<node) # node 삭제
            print("delete",node,"~(1<<node)=",bin(~(1<<node)),"result=",bin(group))
            break
        
    else: return False
        
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if group&(1<<nxt):
                q.append(nxt)
                group &= ~(1<<nxt) # node 삭제
                print("delete",nxt,"~(1<<nxt)=",bin(~(1<<nxt)),"result=",bin(group))
         
    print("terminal=",bin(group))       
    if not group:
        return True
    else:
        return False

def backtracking(group1):
    global ans
    
    if vis[group1]: return
    vis[group1] = True
    
    #group2 = 2**N-1-group1 # 방법1 
    group2 = ~group1+2**N # 방법2: ~ 연산하면 합이 -1이므로 합이 2**N-1이 될 수 있도록 2**N을 더해주었음
    #group2 = ~group1 ### 비트 반전하는법(1의 보수)(~group1은 2의 보수라서 안됨,,,)
    
    
    if bfs(group1) and bfs(group2): # 앞에서 vis[group]해주기 때문에 bfs가 중복연산될 일은 없음
        sum1 = 0
        for node in range(N):
            if group1&(1<<node):
                sum1 += populations[node]
        sum2 = sum(populations)-sum1
        tmp = abs(sum2-sum1)
        ans = min(ans,tmp)

    for nxt in range(N):
        if group1 & (1<<nxt): continue
        backtracking(group1 | (1<<nxt))
        
backtracking(0)
if ans==INF:
    print(-1)
else:
    print(ans)
    


    

