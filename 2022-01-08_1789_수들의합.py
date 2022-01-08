import sys
input = sys.stdin.readline
n = 1
S = int(input())
while n*(n+1)/2 <= S:
    n += 1
print(n-1)
