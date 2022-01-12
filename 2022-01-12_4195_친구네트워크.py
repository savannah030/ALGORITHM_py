import sys
input = sys.stdin.readline

def union_parent(x,y):
    px = find_parent(x)
    py = find_parent(y)
    # 1.
    if px<py: 
        parent[py]=px
        cnt[px]+=cnt[py]
    elif px>py: # else쓰면 안됨! cnt 중복되기 때문
        parent[px]=py
        cnt[py]+=cnt[px]
        
    # 2. #1 대신 이렇게만 써도 정답에는 지장없음 
    '''
    if px!=py: 
        parent[py]=px
        cnt[px]+=cnt[py]
    '''
 

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])

    return parent[x]


for _ in range(int(input())): 
    parent = dict() # 딕셔너리로 관리
    # 자식의 수(자식 늘어날때마다 최상위 부모의 cnt만 늘려줌)
    # 예제 1 최종결과: cnt= {'Fred': 1, 'Barney': 4, 'Betty': 1, 'Wilma': 1}
    # 예제 2 최종결과: cnt= {'Fred': 1, 'Barney': 4, 'Betty': 2, 'Wilma': 1}
    cnt = dict() 

    for f in range(int(input())):  # 친구 관계의 수<=100,000
        people = list(input().split())
        #people = [p.lower() for p in people]
        for p in people:
            if p not in parent: 
                parent[p]=p
                cnt[p]=1
        union_parent(people[0],people[1])
        print(cnt[find_parent(people[0])]) # 최상위 부모의 cnt 출력해야함
        
            
            
            
        
                
        
        
    