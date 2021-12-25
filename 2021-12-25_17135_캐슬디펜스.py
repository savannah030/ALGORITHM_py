# board는 처음 enemys 좌표값 받을 때만 사용했음

import sys
from itertools import combinations
input = sys.stdin.readline
N,M,D = map(int,input().split()) #행,열,공격거리제한

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

enemys_init = []
for i in range(N-1,-1,-1):
    for j in range(M):
        if board[i][j]==1: enemys_init.append( (i,j) ) # 가장 아래쪽부터, 가장 왼쪽부터 탐색

ans = 0
li = [num for num in range(M)]

for combi in combinations(li,3):
    
    archers = [(N,combi[i]) for i in range(3)]
    cnt = 0
    enemys = enemys_init[:]
    
    while len(enemys)>0: 
        
        # 공격대상 정하기
        targets = set()
        for i in range(3): 
            dis = D ############
            cands = []
            for enemy in enemys:
                tmp = abs(enemy[0]-archers[i][0])+abs(enemy[1]-archers[i][1])
                if tmp<=dis:
                    if tmp<dis: 
                        cands = []
                        dis = tmp
                    cands.append((enemy[0],enemy[1]))
            if len(cands)>0:
                target = sorted(cands, key=lambda x:x[1])[0] # 제일 왼쪽에 있는 적 공격
                targets.add(target)
        
        '''
        # 공격대상 정하기
        targets = set()
        for i in range(3):
            CAL = lambda x: abs(x[0]-archers[i][0])+abs(x[1]-archers[i][1]) ### 공격거리 구하는 람다함수
            enemys = sorted(enemys, key=lambda x: CAL(x) ) 
            if CAL(enemys[0])<=D: ############# 주의!!
                MIN = CAL(enemys[0])
                cands = [ enemy for enemy in enemys if CAL(enemy)==MIN ]
                if len(cands)>0:
                    target = sorted(cands, key=lambda x:x[1])[0] # 제일 왼쪽에 있는 적 공격
                    targets.add(target)
        '''
        
        # 공격
        cnt += len(targets)
                
        # 적의 이동
        alives = set(enemys)-targets
        enemys = [ (alive[0]+1,alive[1]) for alive in alives if (alive[0]+1)<N ]
         
    ans = max(ans,cnt)
print(ans)
