from itertools import permutations

def isPrime(num):
    if num==0 or num==1: return False
    for i in range(2,int(num**(1/2))+1):
        if num%i==0: return False
    return True

def solution(numbers):
    answer = set()
    for k in range(1,len(numbers)+1):
        for per in permutations(numbers,k):
            num = int("".join(per))
            if isPrime(num):
                answer.add(num)
                
    return len(answer)