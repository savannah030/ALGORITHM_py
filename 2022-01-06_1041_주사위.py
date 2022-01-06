import sys
input = sys.stdin.readline

N = int(input())
A,B,C,D,E,F = map(int,input().split())

if N==1:
    print(A+B+C+D+E+F-max(A,B,C,D,E,F))
else:
    MIN1 = min(A,B,C,D,E,F) 
    MIN2 = min(A+E,A+C,A+B,A+D, F+E,F+C,F+B,F+D, E+C,B+C,E+D,B+D)
    MIN3 = min(A+E+C,A+B+C,A+E+D,A+B+D, F+E+C,F+B+C,F+E+D,F+B+D)

    ans = 4*MIN3 + 4*MIN2           # 천장꼭지점, 바닥꼭지점
    + 4*(N-2)*MIN1 + 8*(N-2)*MIN2   # 바닥모서리, 그 외 모서리
    + 5*(N-2)**2*MIN1               # 그 외의 면

    print(ans)