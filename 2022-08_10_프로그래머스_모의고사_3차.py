def solution1(a, b, n):
    answer = 0
    while n>=2:
        k = n//a
        if k==0: break
        answer += (k*b)
        n -= k*a
        n += k*b
    
    return answer

print("solution1")
print("19",solution1(2,1,20))
print("9",solution1(3,1,20))

# 프로그래머스 12973 짝지어제거하기와 비슷

# 투 포인터x (시간초과)
def solution2_wrong(ingredient):
    answer = 0

    while len(ingredient)>=4:
        new_ingredient = []
        l = 0
        while l<len(ingredient)-3: # 최악의 경우 처음부터 다시 탐색해야함
            if ingredient[l:l+4]==[1,2,3,1]:
                answer += 1
                print("l=",l)
                new_ingredient += ingredient[:l]
                l += 4
            else:
                l += 1
                
        if new_ingredient:
            new_ingredient += ingredient[l:]
        # [1,2,3,1] 하나도 없으면 
        else:
            break

        ingredient = new_ingredient[:]
    
    return answer

# 스택
def solution2(ingredient):
    
    answer = 0
    stack = []
    for idx in range(len(ingredient)):
        stack.append(ingredient[idx])
        while stack[-4:]==[1,2,3,1]: 
            answer += 1
            for _ in range(4):
                stack.pop()

    return answer

print("solution2")
print("2",solution2([2,1,1,2,3,1,2,3,1])) # 2
print("0",solution2([1,3,2,1,2,1,3,1,2])) # 0

# 테이블 만들어서 쿼리문 만들기(문제 조건 제대로 보기)
def solution3(distance, scope, times):
    tables = [ [[] for _ in range(11)] for _ in range(11) ]
    soldiers = [sorted(scope[i])+times[i] for i in range(len(scope))]
    soldiers = sorted(soldiers,key=lambda x:(x[0],x[1]))
    for (sc1,sc2,work,rest) in soldiers:
        if not tables[work][rest]:
            tables[work][rest].extend([((work+rest)*i+1)+j for i in range((distance-1)//(work+rest)+1) for j in range(work)]) ### 수열 식 
        for pos in range(sc1,sc2+1):
            if pos in tables[work][rest]:
                return pos
    return distance

def solution(distance, scope, times):
    tables = [ [[] for _ in range(11)] for _ in range(11) ]
    soldiers = [sorted(scope[i])+times[i] for i in range(len(scope))]
    soldiers = sorted(soldiers,key=lambda x:(x[0],x[1]))
    for (sc1,sc2,work,rest) in soldiers:
        if not tables[work][rest]:
            tables[work][rest].extend([((work+rest)*i+1)+j for i in range((distance-1)//(work+rest)+1) for j in range(work)])
        for pos in range(sc1,sc2+1):
            if pos in tables[work][rest]:
                return pos
    return distance

print("solution3")
print("8",solution3(10, [[3,4],[5,8]], [[2,5],[4,3]])) # 8
print("12",solution3(12, [[7,8],[4,6],[11,10]], [[2,2],[2,4],[3,3]])) # 12

from collections import deque

def solution4(n, lighthouse):
    answer = 0
    lighthouse = [sorted(l) for l in lighthouse]
    lighthouse = sorted(lighthouse)
    print(lighthouse)
    '''
    graph = [ [] for _ in range(n+1)] # 1번부터 시작
    for [n1,n2] in lighthouse:
        graph[n1].append(n2)
        graph[n2].append(n1)
    print(graph)
    q = deque()
    for node in range(1,n+1):
        if len(graph[node])==1:
            q.append(node)

    lightOn = [False]*(n+1)
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if not lightOn[nxt]:
                lightOn[nxt]=True
                q.append(nxt) 
    '''



    return answer

