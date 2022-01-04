# 각 집중국의 수신 가능 영역의 길이의 합을 최소화 -> 차이가 가장 큰 구간을 끊기
# 인접한 좌표의 차를 모두 구한 다음 제일 큰 K-1개를 뺀 나머지를 더해주면 됨
# (K-1개의 연결고리 끊으면 K개의 덩어리 생김) 
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
pts = list((map(int,input().split())))
pts.sort()
diff = []
l = len(pts)
for n in range(l-1):
    diff.append(pts[n+1]-pts[n])
diff.sort()
# (K-1)개의 연결고리를 끊으면 K개의 덩어리가 생김
print(sum(diff[:len(diff)-(K-1)]))
    