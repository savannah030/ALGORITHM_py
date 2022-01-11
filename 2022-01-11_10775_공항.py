# Union find 문제라고 함
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
for _ in range(P):
    plane = int(input())
    parent = find_emptyGate(plane)
    if parent == 0:
        break
    union_gates(parent,parent-1)
    cnt += 1
print(cnt)
        

