# 큰 숫자가 나오면 걔보다 작은 앞의 수 다 지우기
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
li = list(map(int,input().rstrip()))
stack = [li[0]]
k = 0
idx = N
for n in range(1,N):
    if k==K: 
        idx = n
        break
    if li[n]<=stack[-1]: 
        stack.append(li[n])
    else: #### while문!!
        while k<K and len(stack)>0 and li[n]>stack[-1]:
            stack.pop()
            k += 1
        stack.append(li[n])
    
if k==K:
    print(int(''.join(map(str,stack+li[idx:]))))
else: # for문 끝까지 돌았음 -> 마지막 (K-k)개 숫자가 작아서 stack에 들어간것이므로 빼주기
    print(int(''.join(map(str,stack[:len(stack)-(K-k)]))))

    
    