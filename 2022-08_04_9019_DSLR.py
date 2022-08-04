# 21분 메모리 초과,, 29분 7%에서 틀렸습니다 pypy 제출
import sys
input = sys.stdin.readline
from collections import deque


def cmd_func(n): # str to str
    return [("D",str((2*int(n))%10000)),("S",str(int(n)-1 if int(n)>0 else 9999)),("L",n.zfill(4)[1:]+n.zfill(4)[0]),("R",n.zfill(4)[-1]+n.zfill(4)[:-1])]

for _ in range(int(input())):
    A,B = map(int,input().split())
    # bfs
    q = deque() # str 저장
    q.append(str(A))
    cmds = ["" for _ in range(10000)] # 0~9999

    while q:
        node = q.popleft()
        if int(node)==B:
            print(cmds[B])
            break
        for (cmd,nxt) in cmd_func(node):
            if int(nxt)!=A and not cmds[int(nxt)]:
                cmds[int(nxt)] = cmds[int(node)]+cmd
                q.append(nxt)


    