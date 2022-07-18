def solution(A, K):
    if len(A)>0:
        K = K%len(A)
    return A[-K:]+A[:-K]

print(solution([3, 8, 9, 7, 6],3))
print(solution([0,0,0],1))
print(solution([1,2,3,4],4))