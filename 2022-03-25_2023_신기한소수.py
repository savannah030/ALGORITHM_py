import sys
input = sys.stdin.readline

N = int(input())

# 에라토스테네스의 체(메모리초과)
isPrime = [True]*(10**N)
isPrime[0],isPrime[1]=False,False
for i in range(2,int(len(isPrime)**0.5)+1):
    if isPrime[i]:
        for j in range(i+i,len(isPrime),i): ## 범위조심(i+i부터 False로 바꿔야함)
            isPrime[j]=False

for num in range(10**(N-1),10**N): # N자리 수 중
    for idx in range(1,N+1):
        if not isPrime[int(str(num)[:idx])]:
            break
    else:
        print(num)
        
            

