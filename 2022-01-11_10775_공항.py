# Union find
# Union: gate에 비행기가 도킹한 경우 union_gates(gate,gate-1) 연산
# find: 해당 비행기가 도킹할 수 있는 게이트 찾기
import sys
input = sys.stdin.readline

def find_emptyGate(x): # find_parent
    if gates[x]!=x:
        gates[x]=find_emptyGate(gates[x])
    return gates[x]

def union_gates(a,b): # union_find
    a = find_emptyGate(a)
    b = find_emptyGate(b)
    if a<b:
        gates[b] = a
    else:
        gates[a] = b


G = int(input()) # 1<=게이트의 수<=10^5
P = int(input()) # 1<=비행기의 수<=10^5

gates = [i for i in range(G+1)]

cnt = 0
for p in range(P):
    maxGate = int(input())
    # 그냥 반복문 써서 도킹할 수 있는 게이트 찾으면 O(G) 걸리겠지만 
    # 서로소 집합 알고리즘 사용하면 O(1)에 가능
    enableGate = find_emptyGate(maxGate)
    if enableGate == 0:
        break
    # enableGate에는 p번째 plane이 들어갔으므로 
    # "enableGate-1부터 가능하다는 뜻"의 union_gates를 수행해줘야한다
    union_gates(enableGate,enableGate-1) 
    cnt += 1
print(cnt)
        

