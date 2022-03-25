import sys
input = sys.stdin.readline

N = int(input())

# num이 소수인지 판별하는 함수
def isPrime(num):
    if num==0 or num==1: return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

for num in range(10**(N-1),10**N): # N자리 수 중
    for digit in [10**n for n in range(N)]:
        k = num//digit
        if not isPrime(k):
            break
    else:
        print(num)


            

