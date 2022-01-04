# 큰 숫자가 나오면 걔보다 작은 앞의 수 다 지우기
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
li = list(map(int,input().rstrip()))
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < li[i]:
        stack.pop()
        k -= 1
    stack.append(li[i])

# for문 중간에 빠져나가지 않으니까 무조건 K개 빼주면 되는거임
print(''.join(map(str,stack[:N-K])))


    
    