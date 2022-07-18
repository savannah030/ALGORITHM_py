def solution(A):
    if len(A)==0:
        return 1
    A.sort()
    for idx in range(len(A)):
        if A[idx] != idx+1:
            return idx+1
    return len(A)+1