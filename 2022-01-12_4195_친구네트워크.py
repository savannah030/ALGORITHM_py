# union find
# cnt: 자식의 수(union연산할때마다 최상위 부모의 cnt만 늘려줌)
# 예제 1 최종결과: cnt= {'Fred': 1, 'Barney': 4, 'Betty': 1, 'Wilma': 1}
# 예제 2 최종결과: cnt= {'Fred': 1, 'Barney': 4, 'Betty': 2, 'Wilma': 1}
import sys
input = sys.stdin.readline

def union_parent(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px!=py: 
        parent[py]=px
        cnt[px]+=cnt[py]

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])

    return parent[x]


for _ in range(int(input())): 
    parent = dict() 
    cnt = dict() 

    for f in range(int(input())):  # 친구 관계의 수<=100,000
        people = list(input().split())
        for p in people:
            if p not in parent: # 새로운 사람이면 
                parent[p]=p     # parent 테이블에 등록
                cnt[p]=1        # 친구 수는 1로 초기화
        union_parent(people[0],people[1])
        print(cnt[find_parent(people[0])]) # 최상위 부모의 cnt 출력해야함