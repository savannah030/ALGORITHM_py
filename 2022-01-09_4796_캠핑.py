# 연속하는 P일 중 L일 동안 사용가능, 강산 휴가: V일, 
# 강산이 최대 며칠동안 사용 가능?
import sys
input = sys.stdin.readline

cnt = 0
while True:
    L,P,V = map(int,input().split())
    if L==0 and P==0 and V==0: break
    cnt += 1
    print("Case "+str(cnt)+": "+str(V//P*L+min(V%P,L)))