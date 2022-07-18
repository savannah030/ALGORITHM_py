def solution(A):
    for num in A:
        if A.count(num)%2 == 1:
            return num
     

# 정렬 O(N) or O(N*log(N))
def solution2(A):
    if len(A) == 1:
        return A[0]

    A = sorted(A)

    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        if A[i] != A[i+1]:
            return A[i]
        