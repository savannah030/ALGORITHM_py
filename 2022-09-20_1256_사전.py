# https://mingchin.tistory.com/m/414
# 수도코드
'''
while K and N and M:
    if K>comb(N+M-1,N-1)(az...za...a의 인덱스)
        K번째 문자열은 z로 시작 ( += z )
        K-=comb(N+M-1,N-1) (a로 시작하는 애들 패스)
        M -= 1
    else:
        문자열 a로 시작 ( += a )
        N -= 1
'''
import sys
from math import comb,factorial
input = sys.stdin.readline

N,M,K = map(int,input().split())

if factorial(N+M)/(factorial(N)*factorial(M))<K:
    print(-1)
else:
    answer = ""
    while K and N and M:
        if K>comb(N+M-1,N-1): 
            answer += 'z' 
            K-=comb(N+M-1,N-1) 
            M -= 1
        else:
            answer += 'a'
            N -= 1
    # K==0이라면 나머지 글자는 a...am...m으로 붙여줘야함
    # K!=0이면 N,M 둘 중 하나는 0
    print(answer +'a'*N+'z'*M)
    



# 13분 런타임에러,,, 200C100이어서 그런듯,,,, dp로 풀어야한다고 한다
'''
import sys
from math import factorial
input = sys.stdin.readline

N,M,K = map(int,input().split())

if factorial(N+M)/(factorial(N)*factorial(M))<K:
    print(-1)
else:
    vis = [False]*(1<<(N+M))
    idx = 0

    def makeCombinations(state,cnt):
        
        global idx
        
        if vis[state]: return
        vis[state] = True
        if cnt == N: # a의 개수가 N개이면
            idx += 1
            if idx == K:
                answer = ['z']*(N+M)
                for i in range(N+M):
                    if state & (1<<i):
                        answer[i] = 'a' 
                print(''.join(answer))
                sys.exit(0)
        
        for i in range(N+M):
            if state & (1<<i) : continue
            makeCombinations(state|(1<<i),cnt+1)


    makeCombinations(0,0)
'''

# 16분 메모리 초과
'''
import sys
input = sys.stdin.readline
from itertools import combinations 

N,M,K = map(int,input().split())
li = list(combinations(range(N+M),N))

if len(li)<K:
    print(-1)
else:
    for k,combi in enumerate(li):
        if k==K-1:
            answer = ['z']*(N+M)
            for c in combi:
                answer[c]='a'
            print(''.join(answer)) 
            break
'''