# 팰린드롬인지 ..? No bbbaaabbb <- 팰린드롬이지만 이 경우 맞지x

# 스택 !! 7분
def solution(str):
    stack = []
    for idx,s in enumerate(str):
        if len(stack)>0 and s==stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    if len(stack)==0:
        return 1
    else:
        return 0
   
# 23분 투포인터 노노
def wrong(s):
        
    # 시도1: 그냥 같은 글자 나왔을 때 그 안이 대칭인지(홀수면 바로 out) 이것도 노노노 그냥 정석대로
    l = 0
    while r<len(s)-1 and s[r]!=s[0]:
        r += 1
    if (r-l)%2==0:
        return 0
    # baaccb
    while l<r and s[l]==s[r]:
        l += 1
        r -= 1

    # 시도2    # 투 포인터
    answer = -1
    l = 0
    while l<len(s)-1 and s[l]!=s[l+1]:
        l += 1
        
    # 끝까지 탐색했는데도 붙어있는 짝이 없으면 실패
    if l==len(s)-1:
        return 0
    
    r = l+1
    ## 이렇게 짜면 테스트1 까다로운데...
    
    return answer
