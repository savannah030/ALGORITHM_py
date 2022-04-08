from ast import expr
import sys
input = sys.stdin.readline

# 백트래킹(가지치기 X) 
def makeExpression(idx,mods): 
    global N
    if idx==N-1:
        expr = ''
        for i in range(N-1):
            expr += str(nums[i])
            expr += mods[i]
        expr += str(nums[N-1])
        
        if eval(expr.replace(" ",""))==0:
            print(expr)
        return
        
    for mod in " +-":
        mods.append(mod)
        makeExpression(idx+1,mods[:])
        mods.pop()
    return

for _ in range(int(input())):
    N = int(input())
    nums = [i+1 for i in range(N)]
    makeExpression(0,[])
    print()