# 32분 77%에서 틀렸습니다,, 28번째줄 추가
import sys
input = sys.stdin.readline

N = int(input()) # 노드개수
parent_table = list(map(int,input().split())) # 0번부터시작, 부모가없으면 -1
children_table = [ [] for _ in range(N)]
for node in range(N):
    if parent_table[node]!=-1:
        children_table[parent_table[node]].append(node)
r_node = int(input())

# 자식 노드 재귀적으로 호출하고 children_table 정보 지우기
def remove_child(parent):
    for child in children_table[parent]:
        remove_child(child)
    children_table[parent].clear()

def dfs(node):
    global answer
    for child in children_table[node]:
       dfs(child)
    if node!=r_node and len(children_table[node])==0: # 루트노드를 지운 경우는 여기서 확인
        answer += 1
    
    
remove_child(r_node) # 지울 노드의 자식들 지우기
if parent_table[r_node]!=-1: # 지울 노드 지우기
    children_table[parent_table[r_node]].remove(r_node) 

answer = 0
ancestor = parent_table.index(-1)
dfs(ancestor)
print(answer)



    
