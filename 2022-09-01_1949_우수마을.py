import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

  
def dfs(node):

    select_node, not_select_node = people[node],0
    
    ##### leaf node면 for문 패스
    # node 선택 했으면 child는 무조건 선택x
    # node 선택 안했으면 child는 선택해도 되고, 안해도 되고
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            select_child, not_select_child = dfs(child)
            select_node += not_select_child 
            not_select_node += max(select_child,not_select_child)
        
    return select_node, not_select_node  


N = int(input()) # 노드 수
people = [-1]+list(map(int,input().split())) # 노드값
graph = [ [] for _ in range(N+1) ]
# 작은 노드가 무조건 부모 노드면 -> 1,3 2,3 이렇게 주어지면 트리 못만듦 
# -> 그래프 정보 저장해서 visited로 판별해야함
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
  
visited = [False]*(N+1)
visited[1] = True      
print(max(dfs(1)))

##########
# backup
##########

# 프로그래머스 실전 모의고사 등대 유형
# 1시간 15분,,,
def dfs_backup3(node):
    #tmp = children[node]
    select_node, not_select_node = people[node],0
    
    # child 선택 안했으면 node는 선택해도 되고, 안해도 되고
    # child 선택 했으면 node는 무조건 선택x
    # ->
    # 부모 선택했으면
    for child in graph[node]:
        select_child, not_select_child = dfs_backup3(child)
        select_node += min(select_child,not_select_child)
        
    
    return select_node, not_select_node
        

# 57분
def dfs_backup2(parent):
    print("p=",parent)
    tmp = graph[parent]
    if not tmp:
        return (people[parent],0) # node를 선택했을 때, 아닐 때
    cands = []
    for child in tmp:
        cands.append(dfs_backup2(child))
    


# 자식 중 누적값 최대인 애 더하기
def dfs_backup(parent):
       
        tmp = graph[parent]
        if not tmp:
            return people[parent],0 # node를 선택했을 때, 아닐 때
        
        for child in tmp:
            if_select_parent, if_not_select_parent = dfs_backup(child)
            if people[parent]>if_select_parent: #### 조건식 잘못,,,
                if_select_parent, if_not_select_parent = if_not_select_parent,if_select_parent
                if_select_parent += people[parent]
        print("if_select_child, if_not_select_child=",if_select_parent, if_not_select_parent)
        return if_select_parent, if_not_select_parent