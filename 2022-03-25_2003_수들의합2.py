import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))

answer = 0
end,sum = 0,A[0]
for start in range(N):
    # 1. end를 가능한 만큼 이동시키기
    while sum<M and end<N-1:
        end += 1
        sum += A[end]
    
    # 2. 부분합이 m일때만 카운트
    if sum==M:
        answer += 1
    
    # 3. 맨 앞칸 빼기(빼도 M보다 크다면 계속 for문에서 3만 실행될거임)
    sum -= A[start]
        
print(answer)
    