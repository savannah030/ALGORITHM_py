import sys
input = sys.stdin.readline


def check(str):
    # 붙인 뒤를 확인
    for idx in range(1,len(str)//2+1):
        if str[-idx:]==str[-(idx*2):-idx]:
            return False
    return True
    
def dfs(str): # 백트래킹
    global N
    if len(str)==N:
        print(int(str))
        exit()
    
    for nxt in '123':
        if check(str+nxt):
            dfs(str+nxt)

N = int(input())
dfs("")

