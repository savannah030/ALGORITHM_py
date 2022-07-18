# 38분 (cnt 세는 방법 주의)
from collections import deque

def solution(n, wires):

    answers = []
    
    for idx in range(n-1):
        visited = [False]*n # 0번부터 시작하도록 바꾸기
        newWires = wires[:]
        newWires.pop(idx)
        
        # 인접 행렬로 바꾸기
        matrix = [ [] for _ in range(n)]
        for wire in newWires:
            matrix[wire[0]-1].append(wire[1]-1)
            matrix[wire[1]-1].append(wire[0]-1)
        
        li = [] # 연결되어있는 노드개수 저장할 리스트
        for x in range(n):
            if not visited[x]:
                # bfs
                q = deque()
                q.append(x)
                visited[x]=True
                cnt = 1
                
                while q:
                    node = q.popleft() 
                    for nxt in matrix[node]:
                        if not visited[nxt]:
                            q.append(nxt)
                            visited[nxt]=True
                            cnt += 1
                 
                li.append(cnt)          
                
                            
        answers.append(abs(li[0]-li[1]))
     
    return min(answers)