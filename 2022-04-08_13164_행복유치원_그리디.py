import sys
input = sys.stdin.readline

N,K = map(int,input().split())
students = list(map(int,input().split()))

diff = [students[i+1]-students[i] for i in range(len(students)-1)]
diff.sort()
# 차이가 제일 큰 (K-1) 구간에서 끊으면 K개 조가 만들어짐(2212번 전봇대와 비슷)
print(sum(diff[:len(diff)-K+1]))