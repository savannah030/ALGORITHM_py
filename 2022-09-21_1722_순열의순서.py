import sys
from math import factorial as f
from itertools import permutations 
input = sys.stdin.readline
# 최대한 간단한 규칙 찾기(몫과 나머지로도 충분히 구할 수 있음)
# 복잡해진다는 건 식 잘못세웠다는 뜻 !!
'''
print("4!")
for idx,per in enumerate(permutations(range(1,5))):
    print(idx,per)
0 (1, 2, 3, 4)
1 (1, 2, 4, 3)
2 (1, 3, 2, 4)
3 (1, 3, 4, 2)
4 (1, 4, 2, 3)
5 (1, 4, 3, 2)
--------------
6 (2, 1, 3, 4)
7 (2, 1, 4, 3)
8 (2, 3, 1, 4)
9 (2, 3, 4, 1)
10 (2, 4, 1, 3)
11 (2, 4, 3, 1)
--------------
12 (3, 1, 2, 4)
13 (3, 1, 4, 2)
14 (3, 2, 1, 4)
15 (3, 2, 4, 1)
16 (3, 4, 1, 2)
17 (3, 4, 2, 1)
--------------
18 (4, 1, 2, 3)
19 (4, 1, 3, 2)
20 (4, 2, 1, 3)
21 (4, 2, 3, 1)
22 (4, 3, 1, 2)
23 (4, 3, 2, 1)
'''

N = int(input())
inputs = list(map(int,input().split()))
if inputs[0]==1:
    k = inputs[1]-1
    cand = [i for i in range(1,N+1)]
    ans = []
    for _ in range(N):
        ans.append(cand[k//f(N-1)]) # k//f(N-1) = 그룹 구하기
        del cand[k//f(N-1)]
        k %= f(N-1)
        N -= 1
    print(*ans)
else:
    li = inputs[1:]
    ans = 1 # 첫번째부터 시작
    cand = [i for i in range(1,N+1)]
    for i in range(len(li)):
        item = li[i]
        ans += cand.index(item)*f(len(cand)-1)
        cand.remove(item)
    print(ans)