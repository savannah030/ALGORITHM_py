# parent는 무조건 find_parent 함수를 통해 접근해야함(parent 배열값 바로 접근하면 안됨)
# union 연산도 parent에 대해 하는거임 (두 원소의 'parent 배열' 갱신해줘야함)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m = map(int,input().split()) # 1 ≤ n ≤ 1,000,000), 1 ≤ 연산의개수 m ≤ 100,000
parent = [i for i in range(n+1)]

def union_parent(x,y): 
    x = find_parent(x) 
    y = find_parent(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]


for _ in range(m):
    cmd,a,b = map(int,input().split())
    if cmd == 0:
        union_parent(a,b)
    else: # cmd == 1
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")