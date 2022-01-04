###### rooms도 min_heap으로 관리하는 게 포인트!!! 
# heap(rooms)는 제일 빨리 끝나는 방 확인용&제일 빨리 끝나는 방보다 더 먼저 시작하면 heap에 추가(강의실 추가)
# 최소의 강의실을 이용해야 하기 때문에 무조건 제일 빨리 끝나는 방으로 들어가야함(더 늦게 끝나는 방 확인할 필요가 없음)
import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N):
    S,T = map(int,input().split())
    classes.append((S,T))
classes.sort()

rooms = []
heappush(rooms,classes[0][1])

#### 각각의 class에 대해 한번씩만 확인해주면 됨(while classes: 노놉!)
for n in range(1,N): 
    # 현재 제일 빨리 끝나는 방보다 더 먼저 시작하면 들어갈 수 있는 방 없다는 거니까                    
    if classes[n][0]<rooms[0]:          
        heappush(rooms,classes[n][1])   # 새로운 강의실 만들기
    # 그게 아니면 제일 빨리 끝나는 방에 들어감(최소의 강의실을 이용해야 하기 때문에 더 늦게 끝나는 방 확인할 필요가 없음)
    else:                              
        heappop(rooms)                   
        heappush(rooms,classes[n][1])
    
print(len(rooms))
    

    
    
    
    