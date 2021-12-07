### append, insert 다 리턴형 없음 주의!!
# 톱니바퀴 A를 회전할 때, 
# 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, 
# B는 A가 회전한 방향과 반대방향으로 회전하게 된다.

import sys
input = sys.stdin.readline

wheels = []
for _ in range(4):
    wheels.append(list(map(int,input().rstrip()))) # N극은 0, S극은 1

K = int(input()) # 회전 횟수 1 ≤ K ≤ 100

for _ in range(K): 
    n,dir = map(int,input().split()) # 톱니바퀴 번호, 회전방향(시계 1, 반시계 -1)
    n -= 1                           # 보정(0번부터 시작)
    turn = dict()                    # key=인덱스 value=방향
    turn[n] = dir 
    
    for r in range(n+1,4):                 # 오른쪽에 있는 톱니바퀴 중 회전할 애들
        if wheels[r][6] == wheels[r-1][2]: # 극이 같으면 r보다 오른쪽에 있는 톱니바퀴들은 움직이지 않으므로
            break
        if (r-n)%2==0: turn[r]=dir #같은방향
        else: turn[r]=-dir
        
    for l in range(n-1,-1,-1): # 왼쪽
        if wheels[l][2] == wheels[l+1][6]:
            break
        if (n-l)%2==0: turn[l]=dir #같은방향
        else: turn[l]=-dir

    for idx,dir in turn.items(): 
        if dir==-1: # 반시계방향
            w = wheels[idx][0]
            wheels[idx] = wheels[idx][1:]
            wheels[idx].append(w)  
        else:
            w = wheels[idx][7]
            wheels[idx] = wheels[idx][:7]
            wheels[idx].insert(0,w)
       
answer = 0
for i in range(4):
    #print(wheels)
    if wheels[i][0]==1: # S극이면
        answer += 2**i
print(answer)    