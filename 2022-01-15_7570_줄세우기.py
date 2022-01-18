# children 배열에서 증가하는 번호 빼고는 다 위치 바꿔줘야함
# 즉, 증가하는 수열 중 가장 긴 수열 고르면 됨
# 여기서는 2,3(가장 긴 증가하는 수열) 빼고 1,4,5를 맨앞 또는 맨뒤로 보내야함
'''
children= [5, 2, 4, 1, 3]
idxs= [0, 3, 1, 4, 2, 0] # idxs[n] = n번 어린이의 위치 
'''

import sys
input = sys.stdin.readline

N = int(input()) # 1<=어린이수<=1,000,000
children = list(map(int,input().split()))

idxs = [0]*(N+1)
for i in range(N):
    idxs[children[i]]=i

cnt = 1
longest = 0
for n in range(1,N):
    if idxs[n]<idxs[n+1]:
        cnt += 1
        if cnt>longest:
            longest = cnt
    else:
        cnt = 1
        
print(N-longest)




