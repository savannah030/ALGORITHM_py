def solution(enroll, referral, seller, amount):
    findParent = dict()
    profits = dict()
    # 각 enroll마다 부모가 누군지 딕셔너리에 저장
    # {'john': '-', 'mary': '-', 'edward': 'mary', 'sam': 'edward', 'emily': 'mary', 'jaimie': 'mary', 'tod': 'jaimie', 'young': 'edward'}
    for (e,r) in zip(enroll,referral):
        findParent[e]=r
   
    for (s,a) in zip(seller,amount):
        
        profit = a*100
        
        while True:
            
            # 종료조건(s가 center거나 배분할 금액이 없으면)
            if s not in findParent or profit//10==0:
                if s not in profits:
                    profits[s]=profit
                else:
                    tmp = profits.get(s)
                    profits[s] = (tmp+profit)
                break
            
            parent = findParent[s]
           
            new_profit = profit//10
            remain = profit-new_profit
            
            # 각각의 턴마다 s가 배분받을 금액만 저장(parent의 금액은 저장X)
            if s not in profits:
                profits[s]=remain
            else:
                tmp = profits.get(s)
                profits[s] = (tmp+remain)
           
            # s와 profit 갱신
            s = parent
            profit = new_profit
        
        
    answer = []
    for e in enroll:
        if e not in profits:
            answer.append(0)
        else:
            answer.append(profits[e])
    return answer