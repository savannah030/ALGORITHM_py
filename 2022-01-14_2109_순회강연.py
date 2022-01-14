import sys
from heapq import heappush,heappop
input = sys.stdin.readline

infos = []
for _ in range(int(input())):
    infos.append(tuple(map(int,input().split()))) #(p,d)
infos = sorted(infos, key=lambda x:x[1]) # 데드라인이 급한 순으로 정렬

pays = []
for info in infos:
    heappush(pays,info[0])
    if len(pays)>info[1]:   ############ # pays 배열 중 데드라인을 넘긴 강의가 '하나라도' 있으면
        heappop(pays)                    # 그 중 가장 강연료가 적은 강의를 뺌(pays 배열에는 데드라인 넘긴 강의가 없게 됨)
print(sum(pays))

    
