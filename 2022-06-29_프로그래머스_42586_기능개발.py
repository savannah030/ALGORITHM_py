# 20분
def solution(progresses, speeds):
    
    dDays = []
    for i,p in enumerate(progresses):
        day = 0
        while p<100:
            day += 1
            p += speeds[i]
        dDays.append(day)
    # print(dDays) # 	[5, 10, 1, 1, 20, 1]
    
    # 투 포인터 느낌
    answer = []
    left,right = 0,0
    while left<len(dDays):
        # 오른쪽 dDays 큰 값이 나올 때까지 right 옮기기
        while right<len(dDays)-1 and dDays[right+1]<=dDays[left]: 
            right += 1
        answer.append(right-left+1)
        # left 이동
        left = right+1
    return answer