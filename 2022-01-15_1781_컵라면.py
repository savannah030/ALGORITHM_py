# 왠만하면 heapq 1개만 쓰도록!  
import sys
from heapq import heappush,heappop
input = sys.stdin.readline

homeworks = []
for _ in range(int(input())): # 20만개
    homeworks.append(tuple(map(int,input().split()))) #(데드라인,컵라면수)
homeworks = sorted(homeworks,key=lambda x:x[0]) # 데드라인 급한 순으로 정렬

cups = []
for h in homeworks:
    heappush(cups,h[1])
    if len(cups)>h[0]:
        heappop(cups)
print(sum(cups))

    