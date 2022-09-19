# 10분 32%에서 틀렸습니다
import sys
input = sys.stdin.readline

N = int(input())
table = set()
def backtracking(num):

    if num in table:
        return
    table.add(num)
    for i in range(num%10-1,-1,-1):
        backtracking(num*10+i)

for i in range(9,-1,-1):
    backtracking(i)
    
table = sorted(list(table))
if N>len(table):
    print(-1)
else:
    print(table[N-1])