from itertools import combinations

def solution1(number):
    answer = 0
    for combi in combinations(number,3):
        if sum(combi)==0:
            answer += 1
    return answer


def solution1_2(number):

    answer = []
    
    def make_combinations(idx,li):
    
        if len(li)==3:
            if sum(li)==0:
                answer.append(li)
            return
        for nxt in range(idx+1,len(number)):
            li.append(number[nxt])
            make_combinations(nxt,li[:])
            li.pop()
    
    for st in range(len(number)):
        make_combinations(st,[number[st]])
        
    return len(answer)

print("solution1_2")
print(solution1_2([-3,-2,-1,0,1,2,3]),"5")

# 일일이 set 연산하면 시간초과
def solution2_wrong(topping):

    # 시간초과,,,
    answer = 0
    for cut in range(len(topping)):
        if(len(set(topping[:cut]))==len(set(topping[cut:]))):
            answer += 1
    return answer
    
    
# 각 케이크 토핑의 종류를 '딕셔너리'로 관리
from collections import defaultdict
def solution2(topping):

    cake1 = defaultdict(int)
    cake2 = defaultdict(int)
    for t in topping:
        cake2[t] += 1

    answer = 0
    for cut in topping:
        cake2[cut] -= 1
        if cake2[cut]==0:
            del cake2[cut]
        cake1[cut] += 1
        if len(cake1.keys())==len(cake2.keys()):
            answer += 1
    
    return answer


print("solution2")
print(solution2([1,2,1,3,1,4,1,2]),"2")
    
    
# 적군??
from collections import deque
def solution3(n, roads, sources, destination):

    graph = [ [] for _ in range(n+1)] # 1번부터 시작
    dist = [-1]*(n+1)
    for [n1,n2] in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # bfs
    q = deque()
    q.append(destination)
    dist[destination] = 0
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if dist[nxt]==-1:
                q.append(nxt)
                dist[nxt] = dist[node]+1

    answer = []
    for s in sources:
        answer.append(dist[s])
    return answer
 
print("solution3")   
print(solution3(5,[[1,2],[1,4],[2,4],[2,5],[4,5]],[1,3,5],5),"[2,-1,0]")