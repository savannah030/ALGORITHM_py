# 마감일 늦는 순으로 더하기(과제 개수 많을수록 좋은거니까)
# 제일 마지막날부터 그날 할 수 있는 과제 중 점수가 가장 큰 것만 더하기
import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
works = []
for _ in range(N):
    d,w = map(int,input().split()) # 1 ≤ 과제마감일 ≤ 1000, 1 ≤ 과제의점수 ≤ 100
    heappush(works,(-d,-w)) # 마감일 늦는순으로, 마감일 같으면 점수 큰순으로
   
ans = 0
cnt = -works[0][0] # cnt=제일 마지막날~1일
while True:
    if cnt==0: break # 0일되면 끝
    
    today = []
    # 그날 할 수 있는 과제 중 점수 제일 큰 것만 더하기
    while works and -works[0][0]>=cnt:
        today.append(tuple(heappop(works))) #(-d,-w)
    
    if today:
        today = sorted(today, key=lambda x:-x[1]) # 점수 작은순으로 정렬
        ans -= today.pop()[1]
        for t in today:
            heappush(works,t)
            
    cnt -= 1
       
print(ans)