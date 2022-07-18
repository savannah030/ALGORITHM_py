# 문제 꼼꼼히 확인하는 습관... 24분
def solution(numbers, hand):
    
    l,r = (3,0),(3,2)
    answer = ''
    
    for num in numbers:
        if num==0:
            x,y = 3,1
        else:
            x,y = (num-1)//3,(num-1)%3
            
        if num in [1,4,7]:
            answer += 'L'
        
        elif num in [3,6,9]:
            answer += 'R'

        else: 
            d1 = abs(l[0]-x)+abs(l[1]-y) # 누를번호와 현재 왼손의 거리
            d2 = abs(r[0]-x)+abs(r[1]-y) # 누를번호와 현재 오른손의 거리

            if d1==d2:
                answer += 'L' if hand=="left" else 'R'
            else:
                answer += 'L' if d1<d2 else 'R'
            
        # 손가락 이동  
        if answer[-1]=='L':
            l=(x,y)
        else:
            r=(x,y)
            
    return answer