import sys
input = sys.stdin.readline

N = int(input())

def dfs(num):
    
    # num 소수판별
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return
        
    # 종료조건
    if len(str(num))==N:
        print(num)
        return
    
    # 수 붙여서 dfs 탐색
    for nxt in "1379": # 끝자리가 짝수거나 5면 무조건 소수가 아니므로 확인할 필요없음(가지치기)
        dfs(int(str(num)+nxt))
    
dfs(2)
dfs(3)
dfs(5)
dfs(7)



            

