# 16분 
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
queries = list(map(int,input().split()))


def binary_search(l,r,answer):
    mid = (l+r)//2
    #print("mid=",mid)
    if A[mid]==answer:
        return True
    elif l>r:
        return False
    elif A[mid]<answer:
        return binary_search(mid+1,r,answer)
    else:
        return binary_search(l,mid-1,answer)
    

#print("sorted A=",A)
l,r = 0,len(A)-1
for query in queries:
    if binary_search(l,r,query):
        print(1)
    else:
        print(0)
        
''' # 재귀문 or 반복문 둘 중 하나만 쓰면 됨
def binary_search_wrong(l,r,answer):
    mid = (l+r)//2
    #print("mid=",mid)
    if A[mid]==answer:
        return True
    while l<r:
        if A[mid]<answer:
            answer = binary_search(mid+1,r,answer)
        else:
            answer = binary_search(l,mid-1,answer)
        return answer
    return False
'''