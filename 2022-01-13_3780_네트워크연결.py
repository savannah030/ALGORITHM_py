# I 명령어일때는 dist 초기값만 설정해주고(dist[i] = abs(i-j)%1000)
# E 명령어일때 find_parent함수에서 dist 갱신해줘야함!

import sys
input = sys.stdin.readline
     
# find_parent(x)의 리턴값을 임시로 다른데에(tmp) 저장해야 
# dist[x]는 dist[parent[x](갱신 전 parent[x])] 값 더해줄 수 있음
def find_parent(x):
    if parent[x]==x:
        return x
    tmp = find_parent(parent[x]) 
    dist[x] += dist[parent[x]]   # 내 dist 갱신(parent[x]는 갱신되기 전 값)
    parent[x] = tmp              # 부모값 저장
    return tmp

for _ in range(int(input())):
    N = int(input())                             # 기업의수 4 ≤ N ≤ 20,000
    parent = [i for i in range(N+1)]             # 1번부터 시작
    dist = [0 for i in range(N+1)]
    while True:
        cmds = list(input().split())
        if cmds[0]=='O': 
            break
        
        if cmds[0]=='E':                             #  기업 I와 현재 I의 센터까지의 거리를 출력
            i = int(cmds[1])
            find_parent(i)              
            print(dist[i])
            
        elif cmds[0]=='I':                           #  센터 I를 기업 J에 연결
            i,j = int(cmds[1]),int(cmds[2])
            dist[i] = abs(i-j)%1000                  #  I와 J를 잇는 라인의 길이는 |I – J|(mod 1000)
            parent[i] = j
        
    