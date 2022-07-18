
def solution(N):
    ans,cnt = 0,0
    
    for digit in format(N,'b'):
        if digit=='1':
            if cnt>0:
                ans = max(ans,cnt)
                cnt = 0
        else: # digit = 0
            cnt += 1
            
    return ans

solution(1041)
